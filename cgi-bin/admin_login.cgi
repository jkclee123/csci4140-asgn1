#! /usr/bin/env python
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
db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
cursor = db.cursor()
sql = "select username from account where username = '%s' and password = '%s'"%(username, password)
cursor.execute(sql)
ac = cursor.fetchall()


if ac != []:
	expiration = datetime.datetime.now() + datetime.timedelta(days=30)
	c1 = Cookie.SimpleCookie()
	c2 = Cookie.SimpleCookie()
	c1["username"] = username
	c1["username"]["expires"] = \
	expiration.strftime("%a %d-%b-%Y %H:%M:%S PST")
	c1["username"]["path"] = '/'
	c2["password"] = password
	c2["password"]["expires"] = \
	expiration.strftime("%a %d-%b-%Y %H:%M:%S PST")
	c2["password"]["path"] = '/'
	print c1 
	print c2
	sql = "select file_name from image"
	cursor.execute(sql)
	ac = cursor.fetchall()
	cursor.close()

	try:
		if ac != []:
			for item in ac[0]:
				os.remove(parentdir + '/image/' + item)
	except:
		j = 0
	try:
		os.remove(currentdir + "/hit-count.txt")
	except:
		j = 0

	db = ""
	db = conn.connect(host='172.30.241.99', user='root', passwd='root')
	cursor = db.cursor()
	sql = "DROP DATABASE exampledb"
	cursor.execute(sql)
	db.commit()
	message = ""
else:
	message = "Invalid username or password!"

cursor.close()

html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="refresh" content="0;url=http:/cgi-bin/admin_create.cgi?login=1&message={0}" />
  <title>Processing...</title>
</head>
<body>
</body>
</html>
'''.format(cgi.escape(str(message)))

print "Content-type: text/html\n\n" + html