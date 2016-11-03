#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tools.pyMysqlHelper import connDB
from tools.pyMysqlHelper import executeSQL
from tools.pyMysqlHelper import exeQuery

"""
这个文件是测试写的数据库操作是否正确
"""
host = '127.0.0.1'
user = 'root'
pwd = ''
db = 'test'

cnn, cur = connDB(host, user, pwd, db)

sql = "INSERT INTO `employee`(`name`,`sex`,`age`) VALUES('{}','{}','{}')\
".format('henry', 'man', 26)

# data = executeSQL(cnn, cur, sql)
# if data:
#     print(data)
#     print("OK")
# else:
#     print(data)
#     print("No")

sql = "select name from employee limit 3"

data = exeQuery(cnn, cur, sql)
print(data)
