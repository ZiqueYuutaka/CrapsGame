def getInput():
	rollAgain = ''
	while rollAgain != 'R' and rollAgain != 'r':
		print(rollAgain)
		rollAgain = input('Press \'R\' or \'r\' to roll dice: ')
		if rollAgain == 'R' or rollAgain == 'r':
			print('player rolled dice')
			return rollAgain
		else:
			print('incorrect input')
		print(rollAgain)

isRollAgain()