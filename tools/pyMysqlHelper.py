# -*- coding: utf-8 -*-
"""
@file:  pyMysqlHelper.py
@author: henry
@time: Thu Nov  3 14:21:15 2016
@ python 操作数据库的简单类的封装
"""
import pymysql
import sys


# 连接数据库函数
def connDB(host='127.0.0.1', user='root', pwd='', db='test',
           charset='utf8', port=3306):
    try:
        conn = pymysql.connect(host=host, user=user, password=pwd, db=db,
                               charset=charset, port=port)
        cur = conn.cursor()
        return (conn, cur)
    except Exception as e:
        print("Error:", e)
        sys.exit(0)


# 更新语句，可执行update,insert语句
def executeSQL(cnn, cur, sql):
    try:
        data = cur.execute(sql)
        cnn.commit()
        return data
    except Exception as e:
        print("Error:", e)
        return None
        sys.exit(0)
    finally:
        connClose(cnn, cur)


# 删除语句，可批量删除
def exeDelete(cnn, cur, sql):
    try:
        data = cur.execute(sql)
        cnn.commit()
        return data
    except Exception as e:
        print("Error:", e)
        return None
        sys.exit(0)
    finally:
        connClose(cnn, cur)


# 查询语句
def exeQuery(cnn, cur, sql):
    try:
        cur.execute(sql)
        data = cur.fetchall()
        return data
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        connClose(cnn, cur)


# 关闭所有连接
def connClose(cnn, cur):
    if cur:
        cur.close()
    if cnn:
        cnn.close()
