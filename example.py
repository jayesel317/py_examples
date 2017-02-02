#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

print "hello","World!!!"

counter_numbers = 0
if counter_numbers:
	print "wtf"
else:
	print "fuck uoy mang"
	
counter_numbers = 1
if counter_numbers:
	print "wtf"
else:
	print "fuck me"
	

con = None

try:

	con = mdb.connect('localhost', 'testuser');

	cur = con.cursor()
	cur.execute("SELECT VERSION()")

	data = cur.fetchone()

	print("Database version : %s " % data)

except mdb.Error, e:

	print ("Error %d: %s" % (e.args[0],e.args[1]))
	sys.exit(1)

finally:    

	if con:    
		con.close()
	