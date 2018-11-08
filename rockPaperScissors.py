'''
Rock-Paper-Scissors

Numbers representing Rock-Paper-Scissors:
0: Rock
1: Paper
2: Scissors

Game outcome:
-1: Player loses
 0: Draw
 1: Player wins
'''

import random

#------------------------------------------------------------
# Global Variables
#------------------------------------------------------------
opponentsLastPlay = random.randrange(0, 3)
playStyle = 1
style = 1 #random.randrange(0,2)

#------------------------------------------------------------
# My Functions
#------------------------------------------------------------

# Parse plays (0, 1, 2) into strings (Rock, Paper, Scissors)
def parseToString(plays):
    outputString = []
    for play in plays:
        if( play == 0):
            outputString.append('Rock')
        elif (play == 1):
            outputString.append('Paper')
        elif (play == 2):
            outputString.append('Scissors')
    print(outputString)
    
# Generate plays for opponent (either by random, or with a strategy)
def opponentTurns(lost):
    play = 0
    # Select strategi for opponent
    if (playStyle == 0):
        # Roll a random value: 0, 1 or 2
        play = random.randrange(0, 3)
    else:
        if (style == 1):
            global opponentsLastPlay
            print(opponentsLastPlay)
            play = opponentsLastPlay
            if (lost == 1):
                print('Bot Lost, change symbol')
                play = random.randrange(0, 3)
                while (play == opponentsLastPlay):
                    play = random.randrange(0, 3)
                opponentsLastPlay = play
        else:
            playerLastPlay = 0
            play = playerLastPlay
    return play

# Input of plays of Player 1
def myTurn():
    myTurn = int(input('Enter Play: '))
    if (myTurn > 2 or myTurn < 0):
        myTurn = 0
        print('Error, invalid input. Turn set to zero.')
    return myTurn

# Determine the winner of the game
def calculateWinner(gameResults):
    score = 0
    for res in gameResults:
        score += res
    if(score > 0):
        winner = 'You have won!'
    elif(score < 0):
        winner = 'You have lost!'
    else:
        winner = 'It''s a draw.. everyone loses!'
    return winner

# Loop for every turn of the game and calculate the outcome of the round
def startGame(turns):
    outcome = [0] * turns
    myPlays = [0] * turns
    otherPlays = [0] * turns
    otherPlays[0] = opponentTurns(0)
    
    for x in range (0, turns):
        myPlays[x] = myTurn()
                
        # Determine who has won this round
        if(otherPlays[x] == myPlays[x]):
            outcome[x] = 0
        else:
            if(otherPlays[x] == 0):
                if(myPlays[x] == 1):
                    outcome[x] = 1
                else:
                    outcome[x] = -1
            elif(otherPlays[x] == 1):
                if(myPlays[x] == 2):
                    outcome[x] = 1
                else:
                    outcome[x] = -1
            elif(otherPlays[x] == 2):
                if(myPlays[x] == 0):
                    outcome[x] = 1
                else:
                    outcome[x] = -1
        
        # Calculate opponents next turn
        if (x+1 < turns):
            otherPlays[x+1] = opponentTurns(outcome[x])
            
    parseToString(myPlays)
    parseToString(otherPlays)
    print(outcome)
    return outcome

#------------------------------------------------------------
# Program start
#------------------------------------------------------------
print('Welcome to Rock-Paper-Scissors! \nHow many rounds do you like to play?')
turnSelect = int(input('Turns: '))
outcome = startGame(turnSelect)
print(calculateWinner(outcome))