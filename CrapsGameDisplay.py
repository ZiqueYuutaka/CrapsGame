
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

def printFunds(funds):
	print('Funds:\t$ %.2f' % (funds))

def reset():
	winnings = 0
	score = 0

def printStats(winnings, score):
	print('\nWinnings	=%d'% winnings)
	print('\nScore		=%d'% score)


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
		die1 = random.randint(MIN,MAX)
		die2 = random.randint(MIN,MAX)
		print('die1:\t %d \n' % (die1))
		print('die2:\t %d \n' % (die2))
		print('Total:\t %d' % (die1 + die2))
		totalFunds = totalFunds - 100
#		print('Funds:\t$ %.2f' % (totalFunds))
		printFunds(totalFunds)
		winnings += 1
		score += 1
		printStats(winnings, score)


	elif key == '2':
		print('Display Available Funds\n')
#		print('Funds:\t$ %.2f' % (totalFunds))
		printFunds(totalFunds)
		printStats(winnings, score)
	elif key == '3':
		print('Reset Winnings to Zero')
		totalFunds = 1000
		winnings = 0
		score = 0
	elif key == '4':
		print('Save Name and Score')
	elif key == '5':
		print('Quitting game')
	else:
		print('Incorrect input')

##############	FUNCTIONS	###############
#PRINTING FUNDS
#PLAYING GAME
#RESETING WINNINGS
#SAVE NAME AND SCORE
###########################################