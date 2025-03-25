import random

wins = 0
totalGames = 0
hand = [] # Holds all the cards in current hand
isHard = False # Variable to determine whether a hand is hard
isSoft = False # Variable to determine if the hand is soft

# create a list representing a deck of cards for blackjack, aces will be represented by "a"
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"] * 4
shuffleDeck = []

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
    
# Always hit if your hand is ≤ 19. Stick if your hand is 20 or 21
def policy3(currentHand):
    if calculateSum(currentHand) != 20 or 21:
        return False
    else:
        return True

# Always stick
def policy4(currentHand):
    while hand < 21:
        return False
    
    return True

# Always hit if the dealer's visible card is 10 or an Ace, unless your hand is 21.
def policy5(currentHand):
    False

# Gives a card to a players hand
def dealCard(deck):
    return deck.pop(random.randrange(len(deck)))

# Represents the dealer's hand
def dealer(dealerHand, deck):
    while calculateSum(dealerHand) < 17:
        dealerHand.append(dealCard(deck))

# Shuffles the deck for each new game
def shuffleDeck(deck):
    shuffledDeck = []

    for card in range(0,52):
        shuffledDeck.append(deck.pop(random.randrange(len(deck)))) 

    return shuffledDeck




    






# This might be chopped guys
       
