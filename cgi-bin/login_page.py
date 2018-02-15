#! /usr/bin/env python

import cgi
import cgitb
cgitb.enable()

html = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title>Login</title>
	</head>
	<body>
	<form method="post" action="/cgi-bin/login.py">
	username: <input name="username" type="text"/><br>
	password: <input name="password" type="password"/><br>
	<input name="submit" type="submit" value="LOGIN" />
	</form>

	<body>
	</html>
	'''
header = "Content-type: text/html\n\n"
print header + html