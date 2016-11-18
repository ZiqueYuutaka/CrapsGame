#	This program simulates the craps game

###################IMPORTS#################
import random
###########################################

MIN = 1
MAX = 6
counter = 0

while counter < 20:
	print(random.randint(MIN,MAX), end='\n')
	counter=counter+1


##############FILE SAVE MECHANISM#########

infile = open(r'PlayersAndScores.txt', 'r')
try:
	S = infile.readline()
	print('The file data.txt contains the following:')
	print(S)

finally:
	infile.close()

##########################################

##########################################
if infile.readline() != '':
	#read the next line
	#put it in a string
	#spilt the string on the delimiter
##########################################