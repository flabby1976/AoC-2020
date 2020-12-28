with open('input.txt') as f:
    players_decks = f.read().split('\n\n')

decks = {}
for deck in players_decks:
    player, cards = deck.split(':\n')
    decks[player] = [int(c) for c in cards.split('\n')]

print(decks)
players = list(decks.keys())

round = 1
while True:
    print("\n-- Round {} --".format(round))
    print("{}'s deck: {}".format(players[0], decks[players[0]]))
    print("{}'s deck: {}".format(players[1], decks[players[1]]))
    p0 = decks[players[0]].pop(0)
    p1 = decks[players[1]].pop(0)
    print("{} plays: {}".format(players[0], p0))
    print("{} plays: {}".format(players[1], p1))
    if p0 > p1:
        winner = players[0]
        loser = players[1]
        winnings = [p0, p1]
    else:
        winner = players[1]
        loser = players[0]
        winnings = [p1, p0]

    decks[winner].extend(winnings)
    print("{} wins the round!".format(winner))

    if len(decks[loser])==0:
        break

    round+=1

print("\n== Post-game results ==")
print("{}'s deck: {}".format(players[0], decks[players[0]]))
print("{}'s deck: {}".format(players[1], decks[players[1]]))

print("winner is ", winner)
num_cards = len(decks[winner])

score = 0
for c in range(num_cards):
    print("+ {} * {}".format(decks[winner][c], (num_cards - c)))
    score += decks[winner][c] * (num_cards - c)
print("= {}".format(score))
