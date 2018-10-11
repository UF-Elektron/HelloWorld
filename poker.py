print("*********")
print("P O K E R")
print("*********")
print("EINGABE IHRER KARTEN")
print("Geben Sie alle Karte in absteigender Wertigkeit ein: ")
print()

#Einlesen der Karten
card = [[0 for x in range(2)] for y in range(5)] 
for cardId in range (0, 5):
    for cardEl in range (0, 2):
        print("Karte Nr ", cardId, "Farbe ", cardEl)
        card[cardId][cardEl] = int(input("Wert "))
        

for cardId in range (0, 5):
    print("Karte Nr ", cardId ," Wert = ", card[cardId][0] ," Farbe ", card[cardId][1])

#Bewertung der Hand

result = "Nothing :-("
colourCounter = 0
sameValue = [0 for x in range(15)] 
row = 0
valueOld = card[0][0] + 1 
colourOld = card[0][1]

for cardId in range (0, 5):
    value = card[cardId][0]
    colour = card[cardId][1]
    
    if(valueOld == card[cardId][0] + 1):
        row += 1
    for x in range (0, 14):
        if(x == card[cardId][0]):
            sameValue[x] += 1
            
    if(colour == colourOld):
        colourCounter += 1

    colourOld = colour
    valueOld = card[cardId][0]

    
if(colourCounter == 5):
    result = "Flush"
    if(row == 5):
        result = "Straight Flush"
        if(card[0][0] == 14):
            result = "Royal Flush"
elif row == 5:
    result = "Straight"

highestNumber = 1
highestNumberOld = 1
for x in range (0, 14):
    print(sameValue[x])
    if highestNumber < sameValue[x]:
        highestNumber = sameValue[x]
    elif highestNumberOld < sameValue[x]:
        highestNumberOld = sameValue[x]
        
if highestNumber == 4:
    result = "Four of a kind"
elif highestNumber == 3:
    result = "Three of a kind"
    if highestNumberOld == 2:
        result = "Full House"
elif highestNumber == 2:
    result = "One Pair"
    if highestNumberOld == 2:
        result = "Two Pairs"

print("Your score: ", result)
