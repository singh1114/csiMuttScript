#!/usr/bin/env python

    # -*- coding: utf-8 -*-

"""
* MIT Licensed

* File Name : csimailman.py

* Purpose : This script was made to send mails to the group of students.
			We have the information in the csv file. We need to extract 
			the info of the file. As we don't want people to know the email 
			of each other. This is a shitty idea according to me. But still I 
			am doing it.

* Creation Date : 22-02-2017

* Copyright (c) 2017 Ranvir Singh <ranvir.singh1114@gmail.com>

"""
# For running bash commands import this module
import subprocess

'''
A simple example on how to use subprocess
i=10

for x in range(0, i):
	subprocess.call(["echo", str(x)])
'''

# Read the file where the data is present 
# Data format : 
# First Name : Last Name : Email Address
inputFile = open("new.csv", "r")

# This variable is used to skip the first line
firstLine = True

# Read every line in the csv file
for line in inputFile:
	if(firstLine):
		firstLine = False
		continue
	
	else:
		# split the line by a comma
		words = line.split(",")

		for x in range(0, 3):
			# Remove the " sign and replace it with empty character
			words[x] = words[x].replace('"', '')

		firstName = words[0]

		lastName = words[1]

		email = words[2]

		print firstName + lastName + email

		# Send the mail to everyone using mutt and subprocess
		# Usage : 
		# -s : subject
		# -i : content of body
		# -a : attach file
		subprocess.call(["mutt", "-s", "Update from CSI society, GNDEC", email, "<", "mailContent.txt"])