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
width = form.getvalue("width")
height = form.getvalue("height")
image_filter = form.getvalue("filter")
done = form.getvalue("done")
idd = form.getvalue("id")

os.remove(parentdir + '/image/' + path)

html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="refresh" content="0;url=http:/cgi-bin/edit.cgi?path={0}&filter={1}&width={2}&height={3}&done={4}&id={5}" />
  <title>Processing...</title>
</head>
<body>
</body>
</html>
'''.format(cgi.escape(str(prev)), cgi.escape(""), cgi.escape(str(width)), cgi.escape(str(height)), cgi.escape(str(0)), cgi.escape(str(idd)))

print "Content-type: text/html\n\n" + html