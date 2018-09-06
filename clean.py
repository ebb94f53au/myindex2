import pymysql
import re
import os
base_path = '/home/siyang/site/myblog/myblog/static/media/upload'
def findAndDel(list1,path):
    now1=os.listdir(base_path+path)
    for p in list1:
        if p in now1:
            now1.remove(p)
    for n in now1:
        os.system('rm '+base_path+path+'/'+n)


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='ebb94f53au', db='myblog')
    print('进入成功')
    cur = conn.cursor()
    cur.execute('select img,body from blog_post')
    a = cur.fetchall()
    Bposter = []
    BconImg = []
    for i in range(len(a)):
        if not a[i][0].split('/')[-1] in Bposter:
            Bposter.append(a[i][0].split('/')[-1])
        b = re.findall(r'<img src="../../../../../static/media/upload/blog/context/(.+?)"(?:.+?)/>', a[i][1])
        for one in b:
            if not one in BconImg:
                BconImg.append(one)
    cur.execute('select img,project from portfolio_portfolio')
    a = cur.fetchall()
    Pposter = []
    Pfile = []
    for i in range(len(a)):
        if not a[i][0].split('/')[-1] in Pposter:
            Pposter.append(a[i][0].split('/')[-1])
        if not a[i][1].split('/')[-1] in Pfile:
            Pfile.append(a[i][1].split('/')[-1])

    findAndDel(Bposter,'/blog/poster')
    findAndDel(BconImg,'/blog/context')
    findAndDel(Pposter,'/portfolio/poster')
    findAndDel(Pfile,'/portfolio/file')