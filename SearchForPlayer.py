D={'hello':'world'}

playerExists = 'false'
while playerExists == 'false':
	name = input('Welcome to CRAPS\nPlease enter your name:')
	try:
		D[name]
		print('Player exists')
		playerExists = ''
	except:
		print('Player does not exists')