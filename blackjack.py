import random

wins = 0
totalGames = 0
hand = [] # Holds all the cards in current hand
isHard = False # Variable to determine whether a hand is hard
isSoft = False # Variable to determine if the hand is soft


# Basing on Phil Main definition
# Calculates the current sum of the hand
def calculateSum(hand):
    global isHard
    global isSoft
    isHard = False
    isSoft = False
    sum = 0
    aces = 0  # Count how many aces are present

    for card in hand:
        if card != "a":
            sum += card
        else:
            aces += 1  # Keep track of aces
    
    # Process each Ace
    for i in range(aces):
        if sum + 11 <= 21:
            sum += 11
            isSoft = True  # If at least one Ace is counted as 11, mark it as soft
        else:
            sum += 1
            isHard = True  # If at least one Ace is counted as 1, mark it as hard

    return sum

    
#FIXME - Ask professor if it should stop at 17 even with an ace, 
# Or if it should stop landing at 17 even if an ace is counted as an eleven
# If the hand is >= to 17, then stick otherwise hit
def policy1(currentHand):
    if calculateSum(currentHand) >= 17:
        return True
    else:
        return False

# If the hand is >= 17, is hard, stick. Else hit unless hand = 21
def policy2(currentHand):
    if calculateSum(currentHand) >= 17 and isHard and calculateSum(currentHand) != 21:
        return True
    else:
        return False

# Always stick
def policy4(currentHand):
    while hand < 21:
        return False
    
    return True
    

# create a list representing a deck of cards for blackjack, aces will be represented by "a"
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"] * 4


while (not policy1(hand)):
    hand.append(random.choice(deck))
        
    print(hand)
    print("Soft: ", isSoft)
    print("Hard: ", isHard)
    
        
# This might be chopped guys
       
