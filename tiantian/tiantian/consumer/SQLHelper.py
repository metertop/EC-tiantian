# coding:utf-8

import MySQLdb
from redis import *


class MySQLHelper(object):
    '''数据库的简单封装,调用时只需要修改一下db以及passwd这俩个参数即可!'''
    def __init__(self, host="localhost", port=3306, db="tiantian", user="root",
                 passwd="mysql", charset="utf8"):
        """MySQL 数据库初始化"""
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    def connect(self):
        """连接数据库"""
        self.conn = MySQLdb.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        """关闭数据库"""
        self.cursor.close()
        self.conn.close()

    def insert(self, sql, params=[]):
        """插入一行数据"""
        return self.__execute(sql, params)

    def delete(self, sql, params=[]):
        """删除一行数据"""
        return self.__execute(sql, params)

    def update(self, sql, params=[]):
        """修改一行数据"""
        return self.__execute(sql, params)

    def getFetchOne(self, sql, params=()):
        """查询一条数据"""
        self.connect()
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        self.close()
        return result

    def getFetchAll(self, sql, params):
        """查询多条数据"""
        self.connect()
        self.cursor.execute(sql, params)
        list1 = self.cursor.fetchall()
        self.close()
        return list

    def __execute(self, sql, params):
        """增删改执行的操作"""
        count = 0  # 表示操作sql后变化的行数,默认为0,即没有进行操作
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception, e:
            print(e)
            self.conn.rollback()
        finally:
            self.close()
        return count


class RedisHelper(object):
    """redis 的封装"""
    def __init__(self, host="localhost", port=6379):
        self.__redis = StrictRedis(host, port)

    def get(self, key):
        """redis 通过key获取value"""
        return self.__redis.get(key)

    def set(self, key, value):
        """设置key对应的value"""
        self.__redis.set(key, value)
