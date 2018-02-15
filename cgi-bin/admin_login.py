#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import mysql.connector as conn
import Cookie, os, inspect
import datetime
import random

# add parent dir path to sys.path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

form = cgi.FieldStorage()
username = "Admin"
password = form.getvalue("password")
db = conn.connect(host='localhost', user='root', passwd='', db='exampledb')
cursor = db.cursor()
sql = "select username from account where username = '%s' and password = '%s'"%(username, password)
cursor.execute(sql)
ac = cursor.fetchall()


if ac != []:
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
	sql = "select file_name from image"
	cursor.execute(sql)
	ac = cursor.fetchall()
	cursor.close()

	if ac != []:
		for item in ac[0]:
			os.remove(parentdir + '\image\\' + item)
	try:
		os.remove(currentdir + "\\hit-count.txt")
	except:
		j = 0

	db = ""
	db = conn.connect(host='localhost', user='root', passwd='')
	cursor = db.cursor()
	sql = "DROP DATABASE exampledb"
	cursor.execute(sql)
	db.commit()
	cursor.close()

html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="refresh" content="0;url=http:/cgi-bin/admin_create.py?login=1" />
  <title>Processing...</title>
</head>
<body>
</body>
</html>
'''

print "Content-type: text/html\n\n" + html