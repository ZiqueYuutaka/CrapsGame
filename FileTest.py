# example of file read and write
D = {'steve':(1,1,1000), 'sarah':(0,2,900)}

outfile = open(r'test.txt', 'w')
try:
	print('Saving D to file test.txt')
	for i in D:
		outfile.write(i + '|')
		for val in D[i]:
			outfile.write(str(val) + '|')

finally:
	outfile.close()