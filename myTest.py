# DME, created 21.06.2018
# Brief: This is my very first python program! :D
# Python learning links:
#         List of learning links: https://wiki.python.org/moin/BeginnersGuide/Programmers
#         Learn python step-by-step: http://www.techbeamers.com/python-tutorial-step-by-step/
from cmath import sqrt, cos
from math import acos

def zenRoutine():
    # Type "import this" to print the zen of python
    print('----------------------------------------------------------------')
    import this # This line prints "the zen of python" only the first time it is called (How can I print it again?)
    this    # Here is the call of 'this' not needed. I wrote it to surpress the warning that 'this' was not used
    print('----------------------------------------------------------------')
    
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

def objectExperiments():
    # Current chapter: http://www.techbeamers.com/understand-python-statement-indentation/
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

def randomNumber():
    import random # Import of the random (library?) is needed for random.XYZ to work
    print('Calculate a random number between lower bound and upper bound')
    lowerBound = int(input('lower bound '))
    upperBound = int(input('upper bound '))
    print('%i' %random.randrange(lowerBound, upperBound))
   
def kartesToPolar():
    print('It''s easy to work with complex numbers in Python, because there is a type that suports complex numbers!')
    complexVal = complex(input('Type real value '))
    complexVal = complexVal + complex(input('Type complex value (Format: nj)'))
    print('Real value: %i' %complexVal.real, ' imaginary value: %i' %complexVal.imag)
    betrag = sqrt(pow(complexVal.real, 2) + pow(complexVal.imag, 2))
    betrag = betrag.real
    winkel = acos(complexVal.real / betrag)
    print('Polar form: z = %i' %betrag, ' <%f' %winkel.real)
    
#*****************************************************************************************************************************************************************
# Start of the program:
running = 1

while running:
    print('What do you want to do? \n[0] Exit Program selection \n[1] Start Interest Calculator \n[2] Object experiments \n[3] Print The Zen of Python \n[4] Get random number')
    programSelection = int(input('Type a number to run a program: '))

    if programSelection == 0:   # Exit program selection
        running = 0
        
    elif programSelection == 1: # Start interest calculator (with input and output)
        print('Interest Calculator:')
        amount = float(input('Principal amount ?'))
        roi = float(input('Rate of Interest ?'))
        years = int(input('Duration (no. of years) ?'))
        interestRoutine(amount, roi, years)
    
    elif programSelection == 2: # Start object experiments
        objectExperiments()
        
    elif programSelection == 3: # Start zen routine (import this)
        zenRoutine()
       
    elif programSelection == 4: # Get random number
        randomNumber() 
        
    elif programSelection == 5: # Convert a complex value from cartesian to polar form
        kartesToPolar()
        
    else:
        print('No valid number was printed.. :-( \n')
    
print('\n----End of program----')

