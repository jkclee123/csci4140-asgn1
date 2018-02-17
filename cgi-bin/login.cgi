#! /usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import mysql.connector as conn
import Cookie
import datetime
import random


form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")
db = conn.connect(host='172.30.33.136', user='root', passwd='root', db='exampledb')
cursor = db.cursor()
sql = "select username from account where username = '%s' and password = '%s'"%(username, password)
cursor.execute(sql)
ac = cursor.fetchall()
cursor.close()

if ac != []:
	c1 = Cookie.SimpleCookie()
	c2 = Cookie.SimpleCookie()
	c3 = Cookie.SimpleCookie()
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
  <meta http-equiv="refresh" content="0;url=http:/cgi-bin/index.cgi" />
  <title>Processing...</title>
</head>
<body>
</body>
</html>
'''

print "Content-type: text/html\n\n" + html