import random

wins = 0
totalGames = 0
hand = []
test = 0

# Calculates the current sum of the hand
def calculateSum(hand):
    global test
    sum = 0
    
    for card in hand:
        if card != "a":
            sum += card
        elif card == "a" and sum + 11 <= 21:
            sum += 11
        else:
            sum += 1
    test = sum
    return sum
    
#FIXME - ask professor if it should stop at 17 even with an ace, 
# or if it should stop landing at 17 even if an ace is counted as an eleven
# If the hand is >= to 17, then stick otherwise hit
def policy1(currentHand):
    if calculateSum(currentHand) >= 17:
        return True
    else:
        return False
    

    

# create a list representing a deck of cards for blackjack, aces will be represented by "a"
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"] * 4

for i in range(0,20):
    while (not policy1(hand)):
        hand.append(random.choice(deck))
        
        print(hand)
        
    print(test)
    hand = []
    test = 0
       
