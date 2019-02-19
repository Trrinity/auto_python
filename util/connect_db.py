#!/usr/bin/python
# -*- coding: UTF-8  -*-
import pymysql
import json
class OperationMysql:
	def __init__(self):
		self.conn = pymysql.connect(
			host='13.231.33.161',
			port=3306,
			user='myuser',
			passwd='&&^^',
			db='%%',
			charset='utf8',
			cursorclass=pymysql.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		result = json.dumps(result)
		return result

if __name__ == '__main__':
	op_mysql = OperationMysql()
	res = op_mysql.search_one("select * from user where id=1")
	print (res)
