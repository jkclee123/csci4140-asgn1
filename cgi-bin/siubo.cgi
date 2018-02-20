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

db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
cursor = db.cursor()
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
cursor.close()

html ='''
<!DOCTYPE html>
<html lang="en">
<head>
	<meta http-equiv="refresh" content="0;url=/init.html" />
	<title>Processing...</title>
</head>
<body>
</body>
</html>
'''
print "Content-type: text/html\n\n" + html