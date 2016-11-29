# example of file read and write
L = []

infile = open(r'PlayersAndScores.txt', 'r')
try:
	S = infile.readline()
	print('The file PlayersAndScores.txt contains the following:')
	print(S)
	print('Split string S')
	L = S.split('|')
	print('L contains: ')
	for i in L:
		print(i)

finally:
	infile.close()

outfile = open(r'PlayersAndScores2.txt', 'w')
try:
	print('Saving L to file PlayersAndScores2.txt')
	for i in L:
		outfile.write(i + '|')

finally:
	outfile.close()