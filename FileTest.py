# example of file read and write
D = {'steve':(1000,1,1), 'sarah':(900,0,2)}

outfile = open('test.txt', 'w')
try:
	print('Saving D to file test.txt')
	for i in D:
		tempTup = D[i]
		outfile.write(i + '|' + str(tempTup[2])+ '|' + 
			str(tempTup[1])+ '|' + str(tempTup[0]) + '\n')

finally:
	outfile.close()