inputString = open("Day22Input.txt", "r").read()

player1, player2 = inputString.split("\n\n")
player1 = [int(i) for i in player1.split(":")[1].strip().split("\n")]
player2 = [int(i) for i in player2.split(":")[1].strip().split("\n")]

def scoreDeck(deck):
    return sum([(x+1) * y for x, y in enumerate(deck[::-1])])

def playCombat():
    deck1, deck2 = player1[:], player2[:]
    while len(deck1) > 0 and len(deck2) > 0:
        card1, card2 = deck1.pop(0), deck2.pop(0)
        deck1.extend([card1, card2]) if card1 > card2 else deck2.extend([card2, card1])
    return scoreDeck(deck1) if len(deck1) > 0 else scoreDeck(deck2)

def playRecursiveCombat(deck1, deck2):
    previousScores = set()
    while len(deck1) > 0 and len(deck2) > 0:
        if tuple(deck1) in previousScores or tuple(deck2) in previousScores:
            return 1, 0
        previousScores.add(tuple(deck1))
        previousScores.add(tuple(deck2))
        card1, card2 = deck1.pop(0), deck2.pop(0)
        if len(deck1) < card1 or len(deck2) < card2:
            deck1.extend([card1, card2]) if card1 > card2 else deck2.extend([card2, card1])
        else:
            score1, score2 = playRecursiveCombat(deck1[:card1], deck2[:card2])
            deck1.extend([card1, card2]) if score1 > score2 else deck2.extend([card2, card1])
    return scoreDeck(deck1), scoreDeck(deck2)

print(playCombat())
print(max(playRecursiveCombat(player1[:], player2[:])))
