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

os.remove(parentdir + '\image\\' + path)
try:
	os.remove(parentdir + '\image\\' + prev)
except:
	j = 0
db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
cursor = db.cursor()
sql = "delete from image where id = '%d'" % int(idd)
cursor.execute(sql)
db.commit()
hit_count_path = os.path.join(os.path.dirname(__file__), "hit-count.txt")
if os.path.isfile(hit_count_path):
	hit_count = int(open(hit_count_path).read())
	hit_count -= 1

hit_counter_file = open(hit_count_path, 'w')
hit_counter_file.write(str(hit_count))
hit_counter_file.close()

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