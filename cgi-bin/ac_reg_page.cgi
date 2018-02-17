#! /usr/bin/env python

import cgi
import cgitb
cgitb.enable()

html = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title>Register</title>
	</head>
	<body>

	<form method="post" action="/cgi-bin/ac_reg.py">
	username: <input name="username" type="text" /><br>
	password: <input name="password" type="password" /><br>
	retype password: <input name="re_password" type="password" /><br>
	<input name="submit" type="submit" value="CREATE" />
	</form>
	</body>
	</html>
	'''

header = "Content-type: text/html\n\n"
print header + html