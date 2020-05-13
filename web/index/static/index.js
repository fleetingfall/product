window.onload = function()
{
    $('#priceToSales').linkbutton({
        plain:true,
    });
    $('#priceToMoney').linkbutton({
        plain:true,
    });
    $('#price_rangeToSales').linkbutton({
        plain:true,
    });
    $('#priceToCount').linkbutton({
        plain:true,
    });
    $('#saleaToCount').linkbutton({
        plain:true,
    });
    $('#provinceToCount').linkbutton({
        plain:true,
    });
    $('#top10').linkbutton({
        plain:true,
    });
    $('#map_salea').linkbutton({
        plain:true,
    });
    $('#fuj_sales').linkbutton({
        plain:true,
    });
    $('#zhej_sales').linkbutton({
        plain:true,
    });
    $('#wordcloud').linkbutton({
        plain:true,
    });
    $('#message').linkbutton({
        plain:true,
    });
    $('#update_mes').linkbutton({
        plain:true,
    });
    $('#delete').linkbutton({
        plain:true,
    });

}

function show(name,str){
    $('#content-pic').panel({
        title:name,
        border:false,
        href:str

    });

}



