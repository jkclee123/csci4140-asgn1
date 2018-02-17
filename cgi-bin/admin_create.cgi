#! /usr/bin/env python
import cgi
import cgitb
cgitb.enable()
import mysql.connector as conn
import Cookie, os
import datetime
import random


form = cgi.FieldStorage()
username = "Admin"
password = form.getvalue("password")
re_password = form.getvalue("re_password")
login = form.getvalue("login")

if int(login) == 1:
	cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	db = conn.connect(host='172.30.241.99', user='root', passwd='root')
	cursor = db.cursor()
	sql = "CREATE DATABASE exampledb"
	cursor.execute(sql)
	cursor.close()
	db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
	cursor = db.cursor()
	sql = "CREATE TABLE `account` (`username` varchar(225) NOT NULL,`password` varchar(225) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
	cursor.execute(sql)
	sql = "CREATE TABLE `image` (`file_name` varchar(255) NOT NULL,`username` varchar(255) NOT NULL,`private` int(11) NOT NULL,`permlink` int(11) NOT NULL,`id` int(11) NOT NULL AUTO_INCREMENT,`width` int(11) NOT NULL,`height` int(11) NOT NULL, PRIMARY KEY(`id`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
	cursor.execute(sql)
	sql = "INSERT INTO `account` (`username`, `password`) VALUES ('%s', '%s')"%("Admin", cookie["password"].value)
	cursor.execute(sql)
	db.commit()
	cursor.close()
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
else:
	if password == None or password != re_password:
		html ='''
		<!DOCTYPE html>
		<html lang="en">
		<head>
	  	<meta http-equiv="refresh" content="0;url=http:/cgi-bin/init.cgi" />
	  	<title>Processing...</title>
		</head>
		<body>
		</body>
		</html>
		'''
		print "Content-type: text/html\n\n" + html
	else:
		c1 = Cookie.SimpleCookie()
		c2 = Cookie.SimpleCookie()
		c1["username"] = username
		c1["username"]["expires"] = \
		expiration.strftime("%a %d-%b-%Y %H:%M:%S PST")
		c1["username"]["path"] = '/'
		c2["password"] = password
		c2["password"]["expires"] = \
		expiration.strftime("%a %d-%b-%Y %H:%M:%S PST")
		c2["password"]["path"] = '/'
		print c1 
		print c2
		db = conn.connect(host='172.30.241.99', user='root', passwd='root')
		cursor = db.cursor()
		sql = "CREATE DATABASE exampledb"
		cursor.execute(sql)
		cursor.close()
		db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
		cursor = db.cursor()
		sql = "CREATE TABLE `account` (`username` varchar(225) NOT NULL,`password` varchar(225) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
		cursor.execute(sql)
		sql = "CREATE TABLE `image` (`file_name` varchar(255) NOT NULL,`username` varchar(255) NOT NULL,`private` int(11) NOT NULL,`permlink` int(11) NOT NULL,`id` int(11) NOT NULL AUTO_INCREMENT,`width` int(11) NOT NULL,`height` int(11) NOT NULL, PRIMARY KEY(`id`)) ENGINE=InnoDB DEFAULT CHARSET=latin1;"
		cursor.execute(sql)
		sql = "insert into account (username, password) values ('%s','%s')"%("Admin", str(password))
		cursor.execute(sql)
		db.commit()
		cursor.close()
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