#author: dealthy
#referenced: 
#https://stackoverflow.com/questions/20309456/call-a-function-from-another-file-in-python#20309470

import os

##########user adjustable variables############
class CRUCIALVARIABLES():
	genmaxword = 150
	#random words generated each test: 
	#the less it generates, the faster the loading speed
	timelimit = 60
	#time the testing goes on for
	wordsinline = 10
	#words in each line
	dirpath = os.path.dirname(os.path.realpath(__file__))
	#get current directory