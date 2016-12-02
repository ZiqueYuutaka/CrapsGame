D = {}
tempL = ()

infile = open(r'test.txt', 'r')
try:
	S = infile.readline()
	print('The file test.txt contains the following:')
	print(S)
	print('Split string S')
	L = S.split('|')
	print('L contains: ')
	for i in L:
		print(i)

finally:
	infile.close()