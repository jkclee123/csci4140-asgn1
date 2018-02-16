#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import mysql.connector as conn
import Cookie
import datetime
import random

db = conn.connect(host='localhost', user='root', passwd='')
sql = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'exampledb'"
cursor = db.cursor()
cursor.execute(sql)
database = cursor.fetchall()
cursor.close()
if database != []:
	html = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title>Admin</title>
	</head>
	<body>
		<form method="post" action="/cgi-bin/admin_login.py">
		username: Admin<br>
		password: <input name="password" type="password"/><br>
		<input name="submit" type="submit" value="LOGIN" />
		</form>
		</body>
	</html>
	'''
	header = "Content-type: text/html\n\n"
	print header + html
else:
	html = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title>Admin</title>
	</head>
	<body>
		<form method="post" action="/cgi-bin/admin_create.py?login=0">
		username: Admin<br>
		password: <input name="password" type="password"/><br>
		re-password: <input name="re_password" type="password"/><br>
		<input name="submit" type="submit" value="CREATE" />
		</form>
	</body>
	</html>
	'''
	header = "Content-type: text/html\n\n"
	print header + html
