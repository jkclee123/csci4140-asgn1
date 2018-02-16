#! /usr/bin/env python

import cgi
import cgitb
import Cookie, os
cgitb.enable()

cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])

try:
	html = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title>Update</title>
	</head>
	<body>
	{0}
	<form method="post" action="/cgi-bin/pw_update.py">
	password: <input name="password" type="password"/><br>
	retype password: <input name="re_password" type="password" /><br>
	<input name="submit" type="submit" value="UPDATE" />
	</form>

	<body>
	</html>
	'''.format(cgi.escape(cookie["username"].value))
except(Cookie.CookieError, KeyError):
	html = '''
	<!DOCTYPE html>
	<html lang="en">
	<head>
  	<meta http-equiv="refresh" content="0;url=/cgi-bin/index.py" />
  	<title>Processing</title>
	</head>
	<body>
	</body>
	</html>
	'''

header = "Content-type: text/html\n\n"
print header + html