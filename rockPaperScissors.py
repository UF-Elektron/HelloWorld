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

# Generate random plays for opponent
def opponentTurns(turns):
    plays = [0]*turns
    for x in range(0, turns):
        # Roll a random value: 0, 1 or 2
        plays[x] = random.randrange(0, 3)
    
    print(plays)
    return plays

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
    otherPlays = opponentTurns(turns)
    myPlays = [0] * turns
    outcome = [0] * turns
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
    return outcome

# Program starts:
print('Welcome to Rock-Paper-Scissors! \nHow many rounds do you like to play?')
turnSelect = int(input('Turns: '))
outcome = startGame(turnSelect)
print(calculateWinner(outcome))
