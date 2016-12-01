
players = {}
infile = open('test.txt', 'r')
try:
	S = infile.readline()
	while S != '':
		S=S.rstrip()
		L = S.split('|')
		print(L)
		for i in L:
			players[L.pop()] = (L.pop(),L.pop(),L.pop())
		S = infile.readline()

finally:
	infile.close()

print('printing list L')
print(L)
print('printing keys of D dictionary')
i = 'sarah'
for val in players[i]:
	print(val)
i = 'steve'
for val in players[i]:
	print(val)