
###################IMPORTS#################
import random
###########################################

MIN = 1
MAX = 6
counter = 0

totalFunds = 0
wins = 0
loses = 0
key = ''
playerPoint=0
name = ''

def reset():
	wins = 0
	loses = 0

def printStats(player, funds, wins, loses):
	print('Player:   ' + player)
	print('Funds:  $ %.2f' % (funds))
	print('Wins:     %d'% wins)
	print('Loses:    %d'% loses)

def getInput():
	rollAgain = ''
	while rollAgain != 'R' and rollAgain != 'r':
		rollAgain = input('Press \'R\' or \'r\' to roll dice: ')
		if rollAgain == 'R' or rollAgain == 'r':
			return rollAgain
		else:
			print('incorrect input')

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
	return input('Please enter your name(case sensitive): ')

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

print('Welcome to CRAPS\n')

playerExists = 'false'
while playerExists == 'false':
	name = getName()
	try:
		currentGameStats = ()
		currentGameStats = gameHistory[name]
		print('Welcome back ' + name + '!')
		print('Current Game Stats:')
		totalFunds = int(currentGameStats[0])
		wins = int(currentGameStats[1])
		loses = int(currentGameStats[2])
		printStats(name, totalFunds, wins, loses)
		playerExists = 'true'
	except:
		print('Player does not exists')
		newPlayer = input('Are you a new player? (Y for yes | N for no): ')
		if(newPlayer == 'Y' or newPlayer == 'y'):
			print('Creating new player')
			name = getName()
			totalFunds = 1000
			wins = 0
			loses = 0
			gameHistory[name] = currentGameStats
			playerExists = 'true'
		#else get name

while key != '5':
	print('\n\nCRAPS\n\n\n' +
		  '1\tPlay the game\n'+
		  '2\tDisplay Available Funds\n' +
		  '3\tReset wins to Zero\n' +
		  '4\tSave Name and Score\n' +
		  '5\tQUIT\n\n')
	key = input('Key => ')

	if key == '1':
		print('Play the game\n')

		if(totalFunds <= 0):
			print('GAME OVER-YOU ARE OUT OF FUNDS')
		else:
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
						wins += 1
						playGame = 'false'
					elif (point == 2 or point == 3 or point == 12) and turn == 1:
						print('You rolled a 2, 3 or 12 on turn 1')
						print('YOU LOSE!')
						totalFunds = totalFunds - 100
						loses += 1
						if(totalFunds <= 0):
							print('GAME OVER-YOU ARE OUT OF FUNDS')
							playGame = 'false'
					else: # play using the 'point'
						turn = turn + 1
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
									wins += 1
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
								print('GAME OVER-YOU ARE OUT OF FUNDS')
								playGame = 'false'
								break

		printStats(name, totalFunds, wins, loses)

	elif key == '2':
		print('Display Available Funds\n')
		printStats(name, totalFunds, wins, loses)

	elif key == '3':
		print('Resetting game stats')
		totalFunds = 1000
		wins = 0
		loses = 0
		printStats(name, totalFunds, wins, loses)

	elif key == '4':
		outfile = open(r'PlayersAndScores.txt', 'w')
		try:
			print('Saving current game')
			printStats(name, totalFunds, wins, loses)
			gameHistory[name] = (totalFunds, wins, loses)
			for i in gameHistory:
				tempTup = gameHistory[i]
				outfile.write(i + '|' + str(tempTup[2])+ '|' + 
					str(tempTup[1])+ '|' + str(tempTup[0]) + '\n')
		except:
			print('Error saving data to file')
		finally:
			outfile.close()

	elif key == '5':
		print('Quitting game')
		#are you sure you want to quit
		quitGame = getAnswer()
		if quitGame == 'Y' or quitGame == 'y':
			print('Hope to see you soon')
			printStats(name, totalFunds, wins, loses)
			break
		else:
			key = ''
	else:
		print('Incorrect input: choose a number between 1 and 5')