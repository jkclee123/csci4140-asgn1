#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()
import mysql.connector as conn
import Cookie, os	
import datetime
import random

cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
cookie["username"]["path"] = '/'
cookie["username"]["expires"] = 'Thu, 01 Jan 1970 00:00:00 GMT'
cookie["password"]["path"] = '/'
cookie["password"]["expires"] = 'Thu, 01 Jan 1970 00:00:00 GMT'
print cookie.output()

html ='''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="refresh" content="0;url=http:/cgi-bin/index.py" />
  <title>Processing</title>
</head>
<body>
</body>
</html>
'''

print "Content-type: text/html\n\n" + html