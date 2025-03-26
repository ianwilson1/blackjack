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
    return True
    
# Always hit if the dealer's visible card is 10 or an Ace, unless your hand is 21.
def policy5(currentHand):
    sum = calculateSum(currentHand)
    if dealerCard in [10, "a"] and sum != 21:
        return False  # Hit
    return True  # Stick if it's not dangerous or hand is 21

# Gives a card to a players hand
def dealCard(deck):
    return deck.pop(random.randrange(len(deck)))

# Represents the dealer's hand
def dealer(dealerHand, deck):
    while calculateSum(dealerHand) < 17:
        dealerHand.append(dealCard(deck))
    
    return dealerHand

# Shuffles the deck for each new game
def shuffleDeck(deck):
    shuffledDeck = []
    while deck:  
        shuffledDeck.append(deck.pop(random.randrange(len(deck))))
    return shuffledDeck

def play(policy, deck):
    global wins
    global totalGames
    
    # Initialize each hand
    playerHand = [dealCard(deck), dealCard(deck)]
    dealerHand = [dealCard(deck), dealCard(deck)]

    # Player's turn
    while not policy(playerHand):  # If policy returns False, the player hits
        playerHand.append(dealCard(deck))
        
        if calculateSum(playerHand) > 21:  # Player busts
            totalGames += 1
            return "Loss"
        
    # Dealer's turn (if the player didn't bust)
    dealerHand = dealer(dealerHand, deck)
    
    # Compare hands
    playerTotal = calculateSum(playerHand)
    dealerTotal = calculateSum(dealerHand)
    
    if dealerTotal > 21 or playerTotal > dealerTotal:  # Dealer busts or player wins
        wins += 1
        totalGames += 1
        return "Win"
    elif playerTotal == dealerTotal:
        totalGames += 1
        return "Tie"
    else:
        totalGames += 1
        return "Loss"

def runSimulations(policy, numGames=10000):
    global wins, totalGames, deck
    
    wins = 0
    totalGames = 0
    results = {"Wins": 0, "Losses": 0, "Ties": 0}
    
    for _ in range(numGames):
        # Refresh the deck for each game
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "a"] * 4
        deck = shuffleDeck(deck)
        
        result = play(policy, deck)
        if result == "Win":
            results["Wins"] += 1
        elif result == "Loss":
            results["Losses"] += 1
        elif result == "Tie":
            results["Ties"] += 1
    
    print(f"Results after {numGames} games with this policy:")
    print(f"Wins: {results['Wins']}, Losses: {results['Losses']}, Ties: {results['Ties']}")
    print(f"Win Rate: {results['Wins'] / totalGames * 100:.2f}%")

runSimulations(policy1, 10000)




       
