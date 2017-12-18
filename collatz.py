#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  collatz.py
#  
#  Copyright 2017 Marco Richetta <rich@Compaq>

def collatz(number):
	if number % 2 == 0:
		print number // 2
		return number // 2
	elif number % 2 == 1:
		print 3 * number + 1
		return 3 * number + 1

while True:
	print ("Type a number")
	num = input()
	try:
		if collatz(int(num)) == 1:
			break
	except ValueError:
		print ("Please enter an integer value")


	
