#!/usr/bin/env python
from __future__ import division
import cgi
import cgitb
import Cookie, os, inspect, math
cgitb.enable()
import mysql.connector as conn

# add parent dir path to sys.path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
UPLOAD_DIR = parentdir + '/image/'

db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
cursor = db.cursor()

form = cgi.FieldStorage()
page = form.getvalue("page")
message = form.getvalue("message")

if message == None:
	message = ""
else:
	message = str(message)

if page == None:
	page = 1
else:
	page = int(page)

try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	sql = "select username from account where username = '%s' and password = '%s'"%(cookie["username"].value, cookie["password"].value)
	cursor.execute(sql)
	ac = cursor.fetchall()
	if ac != []:
		login = True
	else:
		login = False
except(Cookie.CookieError, KeyError):
	login = False

if login == True:
	html_head = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title>Index</title>
	</head>
	<body>
	{0}
	&nbsp;
	&nbsp;
	<a href="/cgi-bin/pw_update_page.cgi">Update</a>
	&nbsp;
	&nbsp;
	<a href="/cgi-bin/logout.cgi">Logout</a>
	<br><br>

	<form method="post" action="/cgi-bin/upload.cgi" enctype="multipart/form-data">
	<input type="file" name="file" accept="image/*">
	<select name="private">
  	<option value="1">Private</option>
  	<option value="0">Public</option>
	</select>
	<input type="submit">
	</form>

	'''.format(cgi.escape(cookie["username"].value))

	header = "Content-type: text/html\n\n"
	print header + html_head
	try:
		sql = "select * from image where username = '%s' or private = 0 order by id DESC" %(cookie["username"].value)
		cursor.execute(sql)
		star = cursor.fetchall()

		if page not in range(1, int(math.ceil(len(star) / 8)) + 1):
			page = 1

		if star != []:
			print '<br>'
			for i in range((page - 1) * 8, page  * 8):
				if i >= len(star):
					break
				print '<a href="{0}"><img src="{0}" style="max-width:200px;max-height:200px;"/></a>'.format(cgi.escape("/image/" + str(star[i][0])))
				if (i - 3) % 8 == 0:
					print '<br>'
	except:
		j = 0

else:
	html_head = '''
	<!DOCTYPE html>
	<html>
	<head>
	<title>Index</title>
	</head>
	<body>
	<a href="/cgi-bin/login_page.cgi">Login</a>
	&nbsp;
	&nbsp;
	<a href="/cgi-bin/ac_reg_page.cgi">Create</a>
	<br><br>

	<form action="/cgi-bin/index.cgi" enctype="multipart/form-data">
	<input type="file" name="file" accept="image/*">
	<select name="private">
  	<option value="1">Private</option>
  	<option value="0">Public</option>
	</select>
	<input type="submit">
	</form>
	'''
	header = "Content-type: text/html\n\n"
	print header + html_head
	try:
		sql = "select * from image where private = 0 order by id DESC"
		cursor.execute(sql)
		star = cursor.fetchall()

		if page not in range(0, int(math.ceil(len(star) / 8))):
			page = 1
			
		if star != []:
			print '<br>'
			for i in range((page - 1) * 8, page  * 8):
				if i >= len(star):
					break
				print '<a href="{0}"><img src="{0}" style="max-width:200px;max-height:200px;"/></a>'.format(cgi.escape("/image/" + str(star[i][0])))
				if (i - 3) % 8 == 0:
					print '<br>'
	except:
		j = 0
 

print '<br><br><form>Page: <select name="page">'
for i in range (0, int(math.ceil(len(star) / 8))):
	if i + 1 == page:
		print '<option value="{0}" selected>{0}</option>'.format(cgi.escape(str(i + 1)))	
	else:
  		print '<option value="{0}">{0}</option>'.format(cgi.escape(str(i + 1)))
print '</select>'
print '<input type="submit"/></form>'
if int(page) > 1:
	print '<a href="/cgi-bin/index.cgi?page={0}">Previous</a>'.format(cgi.escape(str(page - 1)))
if int(page) < len(star) / 8:
	print '<a href="/cgi-bin/index.cgi?page={0}">Next</a>'.format(cgi.escape(str(int(page) + 1)))
if message != "":
	print '<br><br>{0}<br>'.format(cgi.escape(strmessage)))


print '''
</body>
</html>
'''