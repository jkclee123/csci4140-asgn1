#! /usr/bin/env python

import cgi
import cgitb
import Cookie, os, inspect, subprocess
cgitb.enable()
import mysql.connector as conn
import random
# add parent dir path to sys.path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
UPLOAD_DIR = parentdir + '/image/'

try:
	form = cgi.FieldStorage()
	form_file = form['file']
	privatee = form.getvalue('private')
	if form_file.filename == None or form_file.filename == "":
		filee = False
	else:
		filee = True
except:
	filee = False

try:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	haha = cookie["username"].value
	login = True
except(Cookie.CookieError, KeyError):
	login = False
if filee == False:
	message = "No file selected!"
if login == False:
	message = "Guests are not allowed to upload!"
if login == False or filee == False:
	print "Content-type: text/html\n\n"
	print '''
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta http-equiv="refresh" content="0;url=/cgi-bin/index.cgi?message={0}" />
	  <title>Fail</title>
	</head>
	<body>
	</body>
	</html>
	'''.format(cgi.escape(message))
else:
	db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
	cursor = db.cursor()
	success = False

	hit_count_path = os.path.join(os.path.dirname(__file__), "hit-count.txt")

	if os.path.isfile(hit_count_path):
	    hit_count = int(open(hit_count_path).read())
	    hit_count += 1
	else:
	    hit_count = 1

	hit_counter_file = open(hit_count_path, 'w')
	hit_counter_file.write(str(hit_count))
	hit_counter_file.close()
	extension = form_file.filename.split('.')
	f = str(hit_count) + '.' + str(extension[1])
	uploaded_file_path = os.path.join(UPLOAD_DIR, os.path.basename(f))

	with file(uploaded_file_path, 'wb') as fout:
		while True:
			chunk = form_file.file.read(100000)
			if not chunk:
				break
			fout.write (chunk)

	try:
		command = ["identify", uploaded_file_path]
		process = subprocess.Popen(command, stdout=subprocess.PIPE)
		output, err = process.communicate()
		h = output.split(" ")
		if h[1].lower() == "jpeg":
			h[1] = "JPG"
		if (h[1].lower() != extension[1]):
			os.remove(uploaded_file_path)
			hit_count = int(open(hit_count_path).read())
			hit_count -= 1
			hit_counter_file = open(hit_count_path, 'w')
			hit_counter_file.write(str(hit_count))
			hit_counter_file.close()
		else:
			g = h[2].split("x")
			sql = "insert into image(file_name, username, private, permlink, width, height) values('%s','%s', '%d', '%d', '%d', '%d')" % (f, cookie["username"].value, int(privatee), 0, int(g[0]), int(g[1]))
			cursor.execute(sql)
			db.commit()
			success = True
	except:
		os.remove(uploaded_file_path)
		hit_count = int(open(hit_count_path).read())
		hit_count -= 1
		hit_counter_file = open(hit_count_path, 'w')
		hit_counter_file.write(str(hit_count))
		hit_counter_file.close()

	cursor.close()

	print "Content-type: text/html\n\n"
	print '''
	<html>
	<head>
	'''
	if success == True:
		print '<meta http-equiv="refresh" content="0;url=http:/cgi-bin/edit.cgi" />'
	else:
		print '<meta http-equiv="refresh" content="0;url=http:/cgi-bin/index.cgi" />'
	print '''
	<title>Uploading</title>
	</head>
	<body>
	'''

	print '</body>'
	print '</html>'

