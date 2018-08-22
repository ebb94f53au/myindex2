
function Submit(path,form) {

//评论提交留言按钮
$.post(path,$(form).serialize(),function(data){
    if (data.status == 'success') {
        alert("提交成功");
//        window.location.href="/contact/"
        location.reload()
                    }
    else{
        alert("提交失败,请检查邮箱格式等");
        location.reload()
    }
})
        }

function TurnPage(turnPath){
//博客跳转按钮
var input_obj =document.getElementById("turnPage")
var turnPage=input_obj.value
var sumPage=input_obj.getAttribute("sum")
if(turnPage<=sumPage&&turnPage>0){
window.location.href=turnPath+"?page="+turnPage

}else{
alert("请输入正确的页数")
}

}
