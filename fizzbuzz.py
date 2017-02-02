#!/usr/bin/python
# -*- coding: utf-8 -*-
def fzbz(my_int):
	#declare indexing variable
	final_int = my_int
	
	#declare some accumulative stats; these are the buckets
	fizzbucket = 0
	buzzbucket = 0
	fizzbuzzbucket = 0
	for num in range(1,final_int):
		if (num % 3 == 0) and (num % 5 == 0):
			print "fizzbuzz"
			fizzbuzzbucket +=1
		elif num % 3 == 0:
			print "fizz"
			fizzbucket +=1
		elif num % 5 == 0:
			print "buzzy"
			buzzbucket +=1
	
	print 'Total FIZZBUZZ: %d	Total FIZZ: %d	Total BUZZ: %d' % (fizzbuzzbucket,fizzbucket,buzzbucket)
