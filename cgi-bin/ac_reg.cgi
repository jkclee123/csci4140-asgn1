#! /usr/bin/env python

import cgi
import cgitb
cgitb.enable()
import mysql.connector as conn
import Cookie, os
import datetime
import random

def connectDB():
	db = conn.connect(host='172.30.33.136', user='root', passwd='root', db='exampledb')
	cursor = db.cursor()
	return db, cursor
	
def insertPeople(db, cursor, username, password):
	sql = "insert into account(username, password) values('%s','%s')" % (username, password)
	cursor.execute(sql)
	db.commit()

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
re_password = form.getvalue("re_password")

db, cursor = connectDB()
sql = "select username from account where username = '%s'"% username
cursor.execute(sql)
ac = cursor.fetchall()


if ac == [] and password == re_password and username != None and password != None:
	insertPeople(db, cursor, username, password)
	c1 = Cookie.SimpleCookie()
	c2 = Cookie.SimpleCookie()
	c1["username"] = username
	c1["username"]["expires"] = 'Tue, 01 Jan 2019 00:00:00 GMT'
	c1["username"]["path"] = '/'
	c2["password"] = password
	c2["password"]["expires"] = 'Tue, 01 Jan 2019 00:00:00 GMT'
	c2["password"]["path"] = '/'
	print c1 
	print c2	

html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="refresh" content="0;url=/cgi-bin/index.cgi" />
  <title>Processing</title>
</head>
<body>
</body>
</html>
'''

cursor.close()
print "Content-type: text/html\n\n" + html