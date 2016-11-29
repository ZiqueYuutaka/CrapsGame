# example of file read and write

infile = open(r'data.txt', 'r')
try:
	S = infile.readline()
	print('The file data.txt contains the following:')
	print(S)

finally:
	infile.close()


outfile = open(r'data.txt','w')
try:
	S2="Poor dan is in a droop"
	outfile.write(S2)

finally:
	outfile.close()

infile2 = open(r'data.txt','r')
try:
	S3 = infile2.readline()
	print('The file data.txt contains the following')
	print(S3)

finally:
	infile2.close()

print('here are your sorted numbers\n')
numbers=[5,1,3,2,4]
numbers.sort()
print(numbers)