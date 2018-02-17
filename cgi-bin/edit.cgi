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

db = conn.connect(host='172.30.241.99', user='root', passwd='root', db='exampledb')
cursor = db.cursor()

print "Content-type: text/html\n\n"
print '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Edit</title>
</head>
<body>
'''

form = cgi.FieldStorage()
prev = form.getvalue("prev")
path = form.getvalue("path")
width = form.getvalue("width")
height = form.getvalue("height")
image_filter = form.getvalue("filter")
done = form.getvalue("done")
idd = form.getvalue("id")

if path == None:
	sql = "select file_name, width, height, id from image order by id DESC limit 1" 
	cursor.execute(sql)
	star = cursor.fetchall()
	path = star[0][0]
	width = int(star[0][1])
	height = int(star[0][2])
	idd = int(star[0][3])
if done == None:
	done = 0
if image_filter == None:
	image_filter = ""

path = str(path)
prev = str(prev)
image_path = "/image/" + str(path)
image_prev = "/image/" + str(prev)
prev_path = parentdir + image_prev
current_path = parentdir + image_path

if image_filter == "border" and int(done) == 0:
	command = ["convert", prev_path, "-bordercolor", "black", "-border", "10", current_path]
if image_filter == "lomo" and int(done) == 0:
	command = ["convert", prev_path, "-channel", "R", "-level", "33%", "-channel", "G", "-level", "33%", current_path]

if image_filter == "lensflare" and int(done) == 0:
	command = ["convert", parentdir + "/image/lensflare.png", "-resize", str(width) + "x", parentdir + "/image/tmp.png"]
	process = subprocess.Popen(command, stdout=subprocess.PIPE)
	command = ["composite", "-compose", "screen", "-gravity", "northwest", parentdir + "/image/tmp.png", prev_path, current_path]

if image_filter == "blackwhite" and int(done) == 0:
	command = ["convert", prev_path, "-type", "grayscale", current_path]
	'''
	process = subprocess.Popen(command, stdout=subprocess.PIPE)
	command = ["convert", parentdir + "/image/bwgrad.png", "-resize", str(width) + "x" + str(height) + "!\\", parentdir + "/image/tmp2.png"]
	process = subprocess.Popen(command, stdout=subprocess.PIPE)
	command = [composite", "-compose", "softlight", "-gravity", "center", parentdir + "/image/tmp2.png", parentdir + "/image/tmp.png", current_path]
	'''

if image_filter == "blur" and int(done) == 0:
	command = ["convert", prev_path, "-blur", "0.5x2", current_path]
if int(done) == 0 and image_filter != "":
	done = 1
	process = subprocess.Popen(command, stdout=subprocess.PIPE)
	#print '<br>{0}<br>'.format(cgi.escape(str(image_path)))
print '<img src="{0}"/><br><br>'.format(cgi.escape(image_path))
if int(done) == 1:
	print '''
	<a href="/cgi-bin/edit.cgi?prev={0}&path={1}&filter={2}&width={3}&height={4}&done={5}&id={6}">Border</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={1}&filter={2}&width={3}&height={4}&done={5}&id={6}">Lomo</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={1}&filter={2}&width={3}&height={4}&done={5}&id={6}">Lens Flare</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={1}&filter={2}&width={3}&height={4}&done={5}&id={6}">Black White</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={1}&filter={2}&width={3}&height={4}&done={5}&id={6}">Blur</a><br><br>
	<a href="/cgi-bin/undo.cgi?prev={0}&path={1}&filter={2}&width={3}&height={4}&done={5}&id={6}">Undo</a><br>
	'''.format(cgi.escape(prev), cgi.escape(path), cgi.escape(""), cgi.escape(str(width)), cgi.escape(str(height)), cgi.escape(str(done)), cgi.escape(str(idd)))
else:
	print '''
	<a href="/cgi-bin/edit.cgi?prev={0}&path={1}&filter={6}&width={11}&height={12}&done={13}&id={15}">Border</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={2}&filter={7}&width={11}&height={12}&done={13}&id={15}">Lomo</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={3}&filter={8}&width={11}&height={12}&done={13}&id={15}">Lens Flare</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={4}&filter={9}&width={11}&height={12}&done={13}&id={15}">Black White</a><br>
	<a href="/cgi-bin/edit.cgi?prev={0}&path={5}&filter={10}&width={11}&height={12}&done={13}&id={15}">Blur</a><br><br>
	<a href="/cgi-bin/edit.cgi?path={0}&filter={14}&width={11}&height={12}&done={13}&id={15}">Undo</a><br>
	'''.format(cgi.escape(path), cgi.escape("border" + path), cgi.escape("lomo" + path), cgi.escape("lensflare" + path), 
		cgi.escape("blackwhite" + path), cgi.escape("blur" + path),cgi.escape("border"), cgi.escape("lomo"), 
		cgi.escape("lensflare"), cgi.escape("blackwhite"), cgi.escape("blur"), cgi.escape(str(width)), cgi.escape(str(height)), cgi.escape(str(done)),
		cgi.escape(""), cgi.escape(str(idd)))

print '<a href="/cgi-bin/discard.cgi?prev={0}&path={1}&id={2}">Discard</a><br>'.format(cgi.escape(prev), cgi.escape(path), cgi.escape(str(idd)))
print '<a href="/cgi-bin/finish.cgi?prev={0}&path={1}&id={2}">Finish</a><br>'.format(cgi.escape(prev), cgi.escape(path), cgi.escape(str(idd)))

print '''
</body>
</html>
'''

