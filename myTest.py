# DME, created 21.06.2018
# Brief: This is my very first python program! :D
# Python learning links:
#        List of learning links: https://wiki.python.org/moin/BeginnersGuide/Programmers
#        New tutorial I work with: https://docs.python.org/3/tutorial/ 

#****************************************************************************************************************
# Imports
#****************************************************************************************************************
# The following imports were automaticly added when I needed these functions
from cmath import sqrt     # for calculation in kartesToPolar()
from math import acos      # for calculation in kartesToPolar()

#****************************************************************************************************************
# My Functions
#****************************************************************************************************************

#----------------------------------------------------------------------------------------------------------------
# Transform a String to ASCII Values (Decimal and Hexadecimal)
#----------------------------------------------------------------------------------------------------------------
def transf(inputText):
    for i in inputText:
        encoded = ord(i)
        print(encoded, hex(encoded))   
    
#----------------------------------------------------------------------------------------------------------------
# Guess a number
#----------------------------------------------------------------------------------------------------------------
def guess():
    import random
    correct = False
    guessCount = 0
    
    # Create random number
    result = random.randrange(0, 100)
    # Expansion for additional feature: Guess a random capital letter
    # A random number in ASCII range for capital letters: result = random.randrange(65, 91)
    # Rewrite input to a number with ord() and output number to a character with chr()
    print('Guess a number between 0 and 100')

    while(correct == False):
        myGuess = int(input('Your guess: '))
        
        # Check if guess is in range
        if(myGuess >= 0 and myGuess <= 100):
            guessCount += 1     # Short for guessCount = guessCount +1
            
            # Guessed number too large, too small or correct?
            if(myGuess > result):
                print('Number too large')
            elif(myGuess < result):
                print('Number too small')
            else:
                correct = True
                print('Result found. Number of guesses: ', guessCount)
                print('---------------------------\n')
        else:
            print('Number outside of range!')
            
#----------------------------------------------------------------------------------------------------------------
# Enocde/Decode a word
#----------------------------------------------------------------------------------------------------------------
def encodeText(inputText, key):
    for i in range (0, len(inputText)):
        encoded = ord(inputText[i]) - key
        print(chr(encoded))
        
def decodeText(inputText, key):
    for i in range (0, len(inputText)):
        decoded = ord(inputText[i]) + key
        print(chr(decoded))
        
#----------------------------------------------------------------------------------------------------------------
# Prints "The zen of python"
#----------------------------------------------------------------------------------------------------------------
def zenRoutine():
    # Type "import this" to print the zen of python
    print('----------------------------------------------------------------')
    import this  # This line prints "the zen of python" only the first time it is called (How can I print it again?)
    this         # Here is the call of 'this' not needed. I wrote it to surpress the warning that 'this' was not used
    print('----------------------------------------------------------------')
    
#----------------------------------------------------------------------------------------------------------------
# Interest calculator: First experimentation with objects
#----------------------------------------------------------------------------------------------------------------
def interestRoutine(amount, roi, years):
    total = (amount * pow(1 + (roi/100), years))
    interest = total - amount
    print('Data type of interest value is', type(interest))
    print('Data type of years value is', type(years))
    
    tmpID = id(years) # Used later to show, that an ID changes after assigning a new value to an object
    
    # Print results
    print('\nInterest = %0.2f' %interest)
    print('\nTotal = %0.2f' %total)
    
    # Show that the type of an object can change during runtime
    print('\nThe Data type of a value can change during runtime. Every value is an object and the datatype of the object can change depending on its assigned value.')
    years = 'Onehundred years'
    print('Assigned new value to variable years: "%s' %years, '"')
    print('Now the datatype of years is ', type(years))
    
    # Show that the id of an object can change during runtime
    print('Also interesting is that when a new value is assigned to an object, then its ID changes (The ID is its address!)')
    print('For example, the old ID of year was: %i' %tmpID, 'and the new one is ', id(years))

#----------------------------------------------------------------------------------------------------------------
# Test the behaviour of objects
#----------------------------------------------------------------------------------------------------------------
def objectExperiments():
    print('Test different features of python objects')
    newVar = 255
    sameVar = 255
    print('The two objects newVar (=%i)' %newVar, 'and sameVar (=%i)'  %sameVar, 'have both stored the same value. And because this value is in the range between -5 and +255 it is stored at the same address.')
    print('This can be seen by checking their IDs: \nnewVar-ID = %i' %id(newVar), '\nsameVar-ID = %i' %id(sameVar))
    print('This concept is known as Interning. It also works for strings wich have less than 20 characters and contain no whitespaces!')
    print('When I create a new object, lets say pointToVar, and set pointToVar = newVar, then they share the same address. But what happens now if i change the value of one of them? Are both of them going to change?')
    pointToVar = newVar
    print('The Value of pointToVar is %i' %pointToVar, 'and its ID is %i' %id(pointToVar))
    pointToVar = 20
    print('Now I changed pointToVar to %i' %pointToVar, 'what is the value of newVar now? newVar = %i' %newVar)
    if pointToVar != newVar:
        print('Ok, so they are not equal.. this means their ID changed! ID of pointToVar %i' %id(pointToVar), 'and ID of newVar %i' %id(newVar))
    else:
        print('Both are equal, so they should still have the same ID. ID of pointToVar %i' %id(pointToVar), 'and ID of newVar %i' %id(newVar))

#----------------------------------------------------------------------------------------------------------------
# Print a random number between two boundaries
#----------------------------------------------------------------------------------------------------------------
def randomNumber():
    import random # Import of the random (library?) is needed for random.XYZ to work
    print('Calculate a random number between lower bound and upper bound')
    try:
        lowerBound = int(input('lower bound '))
        upperBound = int(input('upper bound '))
        print(random.randrange(lowerBound, upperBound))
    except Exception as ex:
        print("Exception ocurred: ", ex)
        
#----------------------------------------------------------------------------------------------------------------
# Transform imaginary values from cartesian to polar form
#----------------------------------------------------------------------------------------------------------------
def kartesToPolar():
    print('It''s easy to work with complex numbers in Python, because there is a type that suports complex numbers!')
    complexVal = complex(input('Type real value '))
    complexVal = complexVal + complex(input('Type complex value (Format: nj)'))
    print('Real value: %i' %complexVal.real, ' imaginary value: %i' %complexVal.imag)
    betrag = sqrt(pow(complexVal.real, 2) + pow(complexVal.imag, 2))
    betrag = betrag.real
    winkel = acos(complexVal.real / betrag)
    print('Polar form: z = %i' %betrag, ' <%f' %winkel.real)
    
#----------------------------------------------------------------------------------------------------------------
# My first list
#----------------------------------------------------------------------------------------------------------------
def listExperiments():
    numberList = [1, 2, 3]   
    stringList = ["alpha", "beta", "gamma"]
    combinedList = numberList + stringList  # Lists can be filled with different data types
    print('The list ', combinedList, 'has %i' %len(combinedList), 'entries.')
    firstLetter = [iterator[0] for iterator in stringList] # This does not work for lists containing numbers!
    print('Print only the first letter of every entry in stringList ', firstLetter)

#----------------------------------------------------------------------------------------------------------------
# Test C-Code LUX interpolation: rewritten to python
#----------------------------------------------------------------------------------------------------------------
def luxInterpolation(adcValue):
    luxLUT = [1, 3, 5, 8, 10, 12, 15, 18, 20, 25, 30, 40, 50, 80, 100, 150, 200, 300, 400, 500, 1000, 1500, 2000, 3000]  # Lux Values 
    adcLUT = [0, 70, 102, 132, 146, 158, 172, 183, 190, 204, 216, 234, 248, 278, 292, 318, 336, 362, 380, 394, 438, 464, 482, 508]     # ADC Values

    for x in range (0, len(luxLUT)):
        if adcValue < adcLUT[x]:
            lutPosition = x
            break
    tempValue = (adcValue- adcLUT[lutPosition-1]*10 / adcLUT[lutPosition] - adcLUT[lutPosition-1])
    result = luxLUT[lutPosition-1] + (luxLUT[lutPosition] - luxLUT[lutPosition-1] * tempValue / 10)
    print('For adcValue = %d' %adcValue, ' result = %d' %result, ' lux')
    
    
#****************************************************************************************************************
# Start of the program:
#****************************************************************************************************************
running = 1

while running:
    print('What do you want to do? \n[0] Exit Program selection \n[1] Start Interest Calculator \n[2] Object experiments \
             \n[3] Print The Zen of Python \n[4] Get random number \n[5] Complex Values \n[6] Start list experiments \
             \n[7] Lux Interpolation \n[8] ASCII encode/decode \n[9] Guess a Number \n[10] Transform string to ASCII')
    programSelection = int(input('Type a number to run a program: '))

    if programSelection == 0:   # Exit program selection
        running = 0
        
    elif programSelection == 1: # Start interest calculator (with input and output)
        print('Interest Calculator:')
        amount = float(input('Principal amount? '))
        roi = float(input('Rate of Interest? '))
        years = int(input('Duration (no. of years)? '))
        interestRoutine(amount, roi, years)
    
    elif programSelection == 2: # Start object experiments
        objectExperiments()
        
    elif programSelection == 3: # Start zen routine (import this)
        zenRoutine()
       
    elif programSelection == 4: # Get random number
        randomNumber() 
        
    elif programSelection == 5: # Convert a complex value from cartesian to polar form
        kartesToPolar()
        
    elif programSelection == 6: # Start list experiments
        listExperiments()
     
    elif programSelection == 7: # Lux Interpolation
        adcTest = [10, 70, 100, 200, 380, 480, 500]
        for x in range (0, len(adcTest)):
            luxInterpolation(adcTest[x])
            
    elif programSelection == 8: # ASCII decode / encode
        inputText = str(input('Word to encode: '))
        inputKey = int(input('Key: '))
        selection = int(input('1: Encode, 2: Decode: '))
        
        if selection == 1:
            encodeText(inputText, inputKey) 
        elif selection == 2:
            decodeText(inputText, inputKey)
        else:
            print('Wrong input')
            
    elif programSelection == 9: # Guess a number
        guess()
    
    elif programSelection == 10:
        transf(input('Input String: '))
        
    else:
        print('No valid number was printed.. :-( \n')
    
print('\n----End of program----')
