# -*- coding:utf-8 -*-
import time
import random


def order_num(package_id=12345, user_id=56789):
    # 商品id后2位+下单时间的年月日12+用户2后四位+随机数4位
    local_time = time.strftime('%Y%m%d%H%M%S')[2:]
    result = str(package_id)[-2:] + local_time +  str(user_id)[-2:] + str(random.randint(1000, 9990))
    return result


if __name__ == '__main__':
    o_num = order_num()
    o_date = time.strftime ("%Y-%m-%d %H:%M:%S")
    print(o_num)