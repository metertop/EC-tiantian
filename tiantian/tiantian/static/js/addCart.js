/**
 * Created by lvhaidong on 2017/1/6.
 */

$(function ()
{
    $num = $('.num_show').val();
    $add = $('.add');
    $minus = $('.minus');
    $total = $('.total em');
    $price = $('.show_pirze em').text();
    $cartNum = $('.goods_count').text();

    // 总价,
    totalPrice = $price * $num
    // 初始化总价格
    $total.text(totalPrice+"	元");

    // ++num => 先自增1,在赋值
    // num++ => 先赋值,在自增1
    // 增加商品
    $add.click(function ()
    {
        $num = $('.num_show').val();
        $('.num_show').val(++$num);
        totalPrice = $price * $num
        $total.text(totalPrice + " 元");
        // $('.goods_count').text($num);
    });

    // 删除商品
    $minus.click(function ()
    {
        $num = $('.num_show').val();
        if ($num > 0)
        {
            $('.num_show').val(--$num);
        }else
        {
            $('.num_show').val(0);
        }
        totalPrice = $price * $num
        $total.text(totalPrice + "元");
        $('.goods_count').text($num);
    });

    // 当用户在输入框中输入一个值,当失去焦点时进行判断
    $('.num_show').blur(function () {

        // 匹配不能以0开头的正整数
        var reg = /^[1-9]\d*$/
        $numText = $('.num_show').val();
        if(!reg.test($numText))
        {
            alert("输入不合法");
            $('.num_show').val(0);
            $total.text(0 + " 元");
        }
        else
        {
            $('.num_show').val($numText);
            totalPrice = $price * $numText
            $total.text(totalPrice + " 元");
            $('.goods_count').text($numText);
        }
        
    });

    // // 立即购买点击事件
    // $('.buy_btn').click(function ()
    // {
    //
    // });



    // 加入购物车点击事件
    $('.add_cart').click(function ()
    {

        // $('.num_show').val(++$num);     // 去掉自增
        totalPrice = $price * $num;
        $total.text(totalPrice + " 元");
        // $('.goods_count').text($num);
        value = $('#goods_id').val();
        $src_count = parseInt($('.goods_count').text());
        // alert($src_count)
        $new_count = $src_count + parseInt($num)  // 添加的时候，数字增加
        $.post('/goods/addCart/',{'num':$num,"value":value},function (data)
        {
            $('.goods_count').text($new_count);

        });
    //    引入外部弹框js  pop_window.js
        new Toast({context:$('body'),message:'成功添加到购物车！'}).show();

    });

    $('.add_goods').click(function ()
    {
        $goodsNum = $('.goods_count').text();
        $('.goods_count').text(++$goodsNum);
    });



});
