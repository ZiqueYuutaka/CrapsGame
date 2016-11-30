
players = {}
infile = open(r'test.txt', 'r')
try:
	S = infile.readline()
	L=[]
	print('The file test.txt contains the following:')
	print(S)
	print('Split string S')
	L = S.split('|')
	print('L contains: ')
	L.pop() #pop blank space
	for i in L:
		players[L.pop()] = (L.pop(),L.pop(),L.pop())

finally:
	infile.close()

print('printing list L')
print(L)
print('printing keys of D dictionary')
i = 'sarah'
print(D.keys())
for val in D[i]:
	print(val)