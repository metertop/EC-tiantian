 $(function(){
        var total = 0;
        var count = 0;

        //定义函数添加total及count
        function total_count(total, count){
            $('.settlements').find('em').text(String(total)+"元"); <!--添加总计金额-->
            $('.settlements').find('b').text(String(count));  <!--添加末尾总数-->
            $('.total_count').find('em').text(String(count));   <!--添加开头总数-->
        }

        //每个商品展示的操作
        $(".cart_list_td").each(function(){
            var price = parseFloat($(this).children(".col05").text())*100;
            var num = parseInt($(this).find(".num_show").attr('value'));
            var subtotal = price*num/100;
            total += subtotal;
            count += num;

            // 在每个ul中添加li小计
            $(this).children(".col07").text(String(subtotal)+'元');
            total_count(total, count);

            // 单选框点击操作,如果checked为true（false），变为false（true），总数count及总价total跟着变化
            $(this).children(".col01").children().click(function(){
                if ($(this).is(":checked")) {
                    $(this).prop("checked",true)
                    count += num
                    total = (total*1000+subtotal*1000)/1000
                    total_count(total, count)
                }
                else {
                    $(this).prop("checked",false)
                    count -= num
                    total = (total*1000-subtotal*1000)/1000
                    total_count(total, count)
                }
            });

            //点击+input的值增加，保存变量为this单选框的状态，点击时，num，subtotal变化，如果checked为true，总数count及total也跟着变
            $(this).find('.add').click(function(){
                var isChecked = $(this).closest("ul").find("input[type=checkbox]").is(":checked");
                num +=1;
                subtotal = price*num/100;
                $(this).next('input').attr({ value: num});
                $(this).closest("ul").find(".col07").text(String(subtotal)+'元');
                if(isChecked){
                    count +=1;
                    total = (total*1000+price*10)/1000;
                    total_count(total, count)
                }
            });

            //点击-input的值减，保存变量为this单选框的状态，点击时，num，subtotal变化，如果checked为true，总数count及total也跟着变
            $(this).find('.minus').click(function(){
                var isChecked = $(this).closest("ul").find("input[type=checkbox]").is(":checked");
                if (num>1){
                    num -= 1;
                    subtotal = price*num/100;
                    $(this).prev('input').attr({ value: num});
                    $(this).closest("ul").find(".col07").text(String(subtotal)+'元');
                    if(isChecked) {
                        count -= 1;
                        total = (total*1000-price*10)/1000;
                        total_count(total, count)
                    }
                }
            });
            //删除操作，点击删除后，total以及count变化，删除this所在的ul所有，向服务器发送ajax数据，删除数据库中相应数据
            var cart_id = $(this).children('.col03').attr('id');
            $(this).children(".col08").children('a').click(function(){
                $(this).closest('ul').remove();
                total = (total*1000 - parseFloat($(this).parent().prev('li').text())*1000)/1000;
                count -= parseInt($(this).closest("ul").find(".num_show").attr('value'));
                total_count(total, count);
                $.post("remove_cart/",
                    {
                    "cartid":cart_id
                    },   function(){
                }
                 );
            });
        });

        //全选、取消全选,此为单独的一个功能模块
        $("#chkall").click(function(){
            var total_1 = 0; //重新获取获取当前所有列表中subtotal的值相加
            var count_1 = 0;//重新获取获取当前所有列表中num的值相加
            $.each($(".col07"), function () {
                total_1 += parseFloat($(this).text().split('元')[0]);

            });
            $.each($(".num_show"), function () {
                count_1 += parseInt($(this).attr("value"))

            });
            if($(this).is(":checked")){
                $(":checkbox").prop("checked",true);

                total_count(total_1, count_1)
            }
            else{
                $(":checkbox").prop("checked",false);
                count = 0;
                total = 0;
                    total_count(total, count)
            }
        });

        //点击提交去结算
        $("ul.settlements").find('a').click(function(){
            var ototal = $('ul.settlements').find('em').text().split('元')[0];
            var cart_id = [];
            var goods = [];
            var countnum = [];
            var price = []
            // each函数取出每个ul中商品的信息，将其组成一个字典，push到列表中

            $(".cart_list_td").each(function(){
                if($(this).children('.col01').children().is(':checked')){
                    cart_id.push($(this).children('.col03').attr('id'));
                    goods.push($(this).children('.col03').text());
                    countnum.push($(this).children('.col06').find('input.num_show').attr('value'));
                    price.push($(this).children('.col05').text().split('元')[0]);
                }
            });
            $.ajax({
                url: '/cart/to_order/',
                data: {
                    "cart_id":cart_id,
                    "ototal":ototal,
                    "goods": goods,
                    "count":countnum,
                    "price":price,
                },
                dataType: "json",
                type: "POST",
                traditional: true,
                success: function (responseJSON) {
                     window.location.href="/order/placeOrder/"
                },
                error: function() {
                    alert('亲，网络出现问题了，请重试！')
                }
            });
        });
 });