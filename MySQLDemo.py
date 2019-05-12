# -*- coding: utf-8 -*-
# @Time    : 2018-3-5 15:38
# @Author  : Amir
# @Site    :
# @File    : ExecelDemo.py
# @Software: PyCharm

import pymysql.cursors


class MySQLDeMo(object):
    def __init__(self, host, port, user, passwd, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.dbName = db
        self.charset = charset

    def Connection(self):
        # 连接数据库
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  passwd=self.passwd,
                                  db=self.dbName,
                                  charset=self.charset)

        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        res = None
        try:
            self.Connection()
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
            self.close()
        except:
            print('查询失败')
        return res

    def get_all(self, sql):
        res = ()
        try:
            self.Connection()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except:
            print('查询失败')
        return res

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            self.Connection()
            count = self.cursor.execute(sql)
            self.db.commit()
            self.close()
        except:
            print('事务提交失败')
            self.db.rollback()
        return count
