
###################IMPORTS#################
import random
###########################################

MIN = 1
MAX = 6
counter = 0

totalFunds = 0
winnings = 0
loses = 0
key = ''
playerPoint=0
name = ''

def printFunds(funds):
	print('Funds:\t$ %.2f' % (funds))

def reset():
	winnings = 0
	loses = 0

def printStats(winnings, loses):
	print('Winnings: %d'% winnings)
	print('Loses:    %d'% loses)

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

def getPlayersFromFile():
	players = {}
	infile = open(r'PlayersAndScores.txt', 'r')
	try:
		S = infile.readline()
		while S != '':
			S=S.rstrip()
			L = S.split('|')
			for i in L:
				players[L.pop()] = (L.pop(),L.pop(),L.pop())
			S = infile.readline()

	finally:
		infile.close()
	return players

def getName():
	return input('Please enter your name: ')

def getAnswer():
	correctInput = 'false'
	x = ''
	while correctInput == 'false':
		x = input('Are you sure you want to quit? (Y for yes | N for no): ')
		if (x != 'Y' and x != 'y') and (x != 'N' and x != 'n'):
			print('Incorrect input')
		else:
			return x


#################################  MAIN GAME  ###########################################

#Read in data before game starts
gameHistory = getPlayersFromFile()

print(gameHistory)
print('Welcome to CRAPS\n')
#Ask player to enter their name

playerExists = 'false'
while playerExists == 'false':
	name = getName()
	try:
		currentGameStats = ()
		currentGameStats = gameHistory[name]
		print('Welcome back ' + name + '!')
		print('Current Game Stats:')
		print('Funds: ' + currentGameStats[0] + '\n' +
			  'Wins: ' + currentGameStats[1] + '\n' +
			  'Loses: ' + currentGameStats[2] + '\n')
		totalFunds = int(currentGameStats[0])
		winnings = int(currentGameStats[1])
		loses = int(currentGameStats[2])
		playerExists = 'true'
	except:
		print('Player does not exists')
		newPlayer = input('Are you a new player? (Y for yes | N for no): ')
		if(newPlayer == 'Y' or newPlayer == 'y'):
			print('Creating new player')
			name = getName()
			#Set current game to default settings
			totalFunds = 0
			winnings = 0
			loses = 0
			gameHistory[name] = currentGameStats
			print(gameHistory[name])
		playerExists = 'true'

while key != '5':
	print('\n\nCRAPS\n\n\n' +
		  '1\tPlay the game\n'+
		  '2\tDispay Available Funds\n' +
		  '3\tReset Winnings to Zero\n' +
		  '4\tSave Name and Score\n' +
		  '5\tQUIT\n\n')
	key = input('Key => ')

	if key == '1':
		print('Play the game\n')

		if(totalFunds <= 0):
			print('You have no available funds to play. Please reset.')
			continue

		roll = ''
		playGame = 'true'
		turn = 1
		point = 0
		while playGame == 'true':
			roll = getInput()
			if(roll == 'R' or roll == 'r'):
				die1 = random.randint(MIN,MAX)
				die2 = random.randint(MIN,MAX)
				point = die1 + die2
				print('die1:\t %d \n' % (die1))
				print('die2:\t %d \n' % (die2))
				print('Roll Total:\t %d' % (point))
				if (point == 7 or point == 11) and turn == 1:
					print('You rolled a 7 or 11 on turn 1')
					print('YOU WIN!')
					totalFunds = totalFunds + 100
					winnings += 1
					playGame = 'false'
				elif (point == 2 or point == 3 or point == 12) and turn == 1:
					print('You rolled a 2, 3 or 12 on turn 1')
					print('YOU LOSE!')
					totalFunds = totalFunds - 100
					loses += 1
					playGame = 'false'
				else: # play using the 'point'
					turn = turn + 1
					#DEBUG
					print('DEBUG Turn num: %d' % (turn))
					print('Roll until you get a %d' % (point))
					while playGame == 'true':
						roll = getInput()
						if(roll == 'R' or roll == 'r'):
							die1 = random.randint(MIN,MAX)
							die2 = random.randint(MIN,MAX)
							print('You rolled a:\t %d' % (die1 + die2))
							if(point == (die1 + die2)):
								print('YOU WIN!')
								playGame = 'false'
								rollAgain = 'false'
								totalFunds = totalFunds  + 100
								winnings += 1
							elif((die1 + die2) == 7):
								print('YOU LOSE!')
								print('You rolled a 7')
								playGame = 'false'
								rollAgain = 'false'
								totalFunds = totalFunds - 100
								loses += 1
							else:
								print('Roll till you get a %d!\n' % (point))
						if(totalFunds <= 0):
							print('You have no available funds left to play')
							playGame = 'false'
							break

		printFunds(totalFunds)
		printStats(winnings, loses)

	elif key == '2':
		print('Display Available Funds\n')
		print('Funds:\t$ %.2f' % (totalFunds))
		printStats(winnings, loses)

	elif key == '3':
		print('Reset Winnings to Zero')
		totalFunds = 1000
		winnings = 0
		loses = 0

	elif key == '4':
		print('Save Name and Score')
		outfile = open(r'PlayersAndScores.txt', 'w')
		try:
			print('Saving gameHistory to file PlayersAndScores.txt')
			gameHistory[name] = (totalFunds, winnings, loses)
			print(gameHistory[name])
			for i in gameHistory:
				tempTup = gameHistory[i]
				outfile.write(i + '|' + str(tempTup[2])+ '|' + 
					str(tempTup[1])+ '|' + str(tempTup[0]) + '\n')

		finally:
			outfile.close()

	elif key == '5':
		print('Quitting game')
		#are you sure you want to quit
		quitGame = getAnswer()
		if quitGame == 'Y' or quitGame == 'y':
			break
		else:
			key = ''
	else:
		print('Incorrect input: choose a number between 1 and 5')