from random import randint

#Gets the string name of an int representing P/S/R
def getHandFromInt(hand):
    if hand == 1:
        return "Paper"
    elif hand == 2:
        return "Scissors"
    elif hand == 3:
        return "Rock"

#Gets the winning hand from two ints representing P/S/R
#Returns the 1 for hand 1, 2 for hand 2, or 0 for draw
def getWinnerFromInts(hand1, hand2):
    if hand1 == hand2:
        return 0
    elif hand1 > hand2 or (hand1 == 1 and hand2 == 3):
        return 1
    else:
        return 2
    
playing = True
print("Welcome to paper-scissors-rock")
while playing:
    print("Choose a hand: ")
    gotHand = False
    hand = 0
    while not gotHand:
        print("1) Paper\n2) Scissors\n3) Rock")
        handInput = input()
        gotHand = True
        if "1" in handInput:
            hand = 1
        elif "2" in handInput:
            hand = 2
        elif "3" in handInput:
            hand = 3
        else:
            print("Sorry, I couldn't recognise that input")
            print("Please select a number from the list")
            gotHand = False
    myHand = randint(1,3)
    print("You chose {} against my {}".format(getHandFromInt(hand), getHandFromInt(myHand)))
    winner = getWinnerFromInts(hand, myHand)
    if winner == 1:
        print("You win!")
    elif winner == 2:
        print("I win!")
    else:
        print("We draw!")
    gotPlayAgain = False
    while not gotPlayAgain:
        print("Play again? (Y/N)")
        reply = input().upper()
        gotPlayAgain = True
        if "N" in reply:
            playing = False
        elif "Y" not in reply:
            print("Sorry, I couldn't recognise that input")
            gotPlayAgain = False
    
