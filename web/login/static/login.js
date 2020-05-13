window.onload = function()
{
    var img = document.getElementById("img_code");
    refreshCode(img);
}

function refreshCode(img)
{
    var t = (new Date()).getTime();
    var code = "/tea/login/code?k=" + t;
    img.src = code;
}