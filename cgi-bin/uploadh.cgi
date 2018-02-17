#!/usr/bin/env python
from __future__ import division
import cgi
import cgitb
import Cookie, os, inspect, math
cgitb.enable()
import mysql.connector as conn
print "Content-type: text/html\n\n"
print '''
<!DOCTYPE html>
<html>
<head>
  <title>Upload File</title>
</head>
<body>
  <h1>Upload File</h1>
  <form action="cgi-bin/uploadd.cgi" method="POST" enctype="multipart/form-data">
    File: <input name="file" type="file" accept="image/*">
    <input name="submit" type="submit">
  </form>
</body>
</html>
'''