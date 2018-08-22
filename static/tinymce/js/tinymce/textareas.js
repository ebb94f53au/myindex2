tinymce.init({
    selector: 'textarea',
    theme : "modern",
    plugins: ["image"],
    language:'zh_CN',
    paste_data_images:true,
    height:'500px',
    width:'1000px',
    file_browser_callback: function(field_name, url, type, win) {
    if(type=='image') $('#my_form input').click();
    },
    });
    $( document ).ready(function() {
    h ='<iframe id="form_target" name="form_target" style="display:none"></iframe><form id="my_form" action="/blog/uploadIMG/" target="form_target" method="post" enctype="multipart/form-data" style="width:0px;height:0;overflow:hidden"><input name="img" type="file" onchange="$(\'#my_form\').submit();this.value=\'\';"></form>';
    $('body').append(h);
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
    // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
    }
    }
    }
    return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken);
    $('#my_form').append('<input type="hidden" name="csrfmiddlewaretoken" value='+csrftoken+' />');

});