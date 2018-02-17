#! /usr/bin/env python
from __future__ import division
import cgi
import cgitb
import Cookie, os, inspect, math, subprocess
cgitb.enable()
import mysql.connector as conn

# add parent dir path to sys.path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

form = cgi.FieldStorage()
prev = form.getvalue("prev")
path = form.getvalue("path")
idd = form.getvalue("id")
prev = str(prev)
image_path = "\image\\" + str(path)

try:
	os.remove(parentdir + '\image\\' + prev)
except:
	j = 0
db = conn.connect(host='localhost', user='root', passwd='', db='exampledb')
cursor = db.cursor()
sql = "update image set file_name = '%s', permlink = '1' where id = '%d'"%(str(path), int(idd))
cursor.execute(sql)
db.commit()

html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Success</title>
</head>
<body>
<img src="{0}"/><br><br>
<a href="{1}">{1}</a><br>
<br>
<a href="/cgi-bin/index.py">Back</a><br>
</body>
</html>
'''.format(cgi.escape(image_path), cgi.escape("/image/" + str(path)))

print "Content-type: text/html\n\n" + html