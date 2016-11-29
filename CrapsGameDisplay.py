
###################IMPORTS#################
import random
###########################################

MIN = 1
MAX = 6
counter = 0

totalFunds = 1000

winnings = 0
score = 0
key = ''
playerPoint=0

def printFunds(funds):
	print('Funds:\t$ %.2f' % (funds))

def reset():
	winnings = 0
	score = 0

def printStats(winnings, score):
	print('Winnings: %d'% winnings)
	print('Score:    %d'% score)

def errorMsg():
	print('Incorrect input')

#def playToPoint(point, ):
	



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

		roll = ''
		playGame = 'true'
		turn = 1
		point = 0
		while playGame == 'true':
			roll = input('Press R/r to roll the dice: ')
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
					score += 1
					playGame = 'false'
				elif (point == 2 or point == 3 or point == 12) and turn == 1:
					print('You rolled a 2, 3 or 12 on turn 1')
					print('YOU LOSE!')
					totalFunds = totalFunds - 100
					playGame = 'false'
				else: # play using the 'point'
					turn = turn + 1
					#DEBUG
					print('DEBUG Turn num: %d' % (turn))
					print('Roll until you get a %d' % (point))
					rollAgain = 'true'
					while rollAgain == 'true':
						roll = input('Press R/r to roll the dice: ')
						if(roll == 'R' or roll == 'r'):
							die1 = random.randint(MIN,MAX)
							die2 = random.randint(MIN,MAX)
							print('Roll Total:\t %d' % (die1 + die2))
							if(point == (die1 + die2)):
								print('YOU WIN!')
								playGame = 'false'
								rollAgain = 'false'
								totalFunds = totalFunds  + 100
							elif((die1 + die2) == 7 or totalFunds <= 0):
								print('YOU LOSE!')
								playGame = 'false'
								rollAgain = 'false'
								totalFunds = totalFunds - 100
							else:
								print('Roll again!\n')
						else:
							errorMsg()
					#End while

			else:
				errorMsg()

		printFunds(totalFunds)
		printStats(winnings, score)


	elif key == '2':
		print('Display Available Funds\n')
		print('Funds:\t$ %.2f' % (totalFunds))
		printStats(winnings, score)

	elif key == '3':
		print('Reset Winnings to Zero')
		totalFunds = 1000
		winnings = 0
		score = 0
	elif key == '4':
		print('Save Name and Score')
		outfile = open(r'PlayersAndScores.txt','w')
		try:
			outfile.write(S2)

		finally:
			outfile.close()
	elif key == '5':
		print('Quitting game')
	else:
		errorMsg()

##############	FUNCTIONS	###############
#PRINTING FUNDS
#PLAYING GAME
#RESETING WINNINGS
#SAVE NAME AND SCORE
###########################################