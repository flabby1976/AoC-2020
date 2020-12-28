import copy

with open('input.txt') as f:
    players_decks = f.read().split('\n\n')

decks = {}

for deck in players_decks:
    player, cards = deck.split(':\n')
    decks[player] = [int(c) for c in cards.split('\n')]

def play_combat(decks, game):

    # print("=== Game {} ===".format(game))

    history = []
    players = list(decks.keys())
    round = 1

    while True:
        if decks in history:
            # print(history, decks)
            # input()
            return players[0]
        else:
            history.append(copy.deepcopy(decks))
            # print(history)
            # print("\n-- Round {} (Game {}) --".format(round, game))
            # print("{}'s deck: {}".format(players[0], decks[players[0]]))
            # print("{}'s deck: {}".format(players[1], decks[players[1]]))
            p0 = decks[players[0]].pop(0)
            p1 = decks[players[1]].pop(0)
            # print("{} plays: {}".format(players[0], p0))
            # print("{} plays: {}".format(players[1], p1))

            if p0 > len(decks[players[0]]) or p1 > len(decks[players[1]]):
                if p0 > p1:
                    winner = players[0]
                else:
                    winner = players[1]
            else: # play recursive game
                # print("Playing a sub-game to determine the winner...")
                n_decks = copy.deepcopy(decks)

                n_decks[players[0]] = n_decks[players[0]][:p0]
                n_decks[players[1]] = n_decks[players[1]][:p1]
                winner = play_combat(n_decks, game+1)
                # print("\n...anyway, back to game {}.", game)

            if winner == players[0]:
                winnings = [p0, p1]
            else:
                winnings = [p1, p0]
            decks[winner].extend(winnings)
            # print("{} wins round {} of game {}!".format(winner, round, game))

            if len(decks[players[0]])==0 or len(decks[players[1]])==0:
                break

            round+=1

    # print("The winner of game {} is {}!".format(game, winner))

    return winner

winner = play_combat(decks, 1)

# players = list(decks.keys())
# print("\n== Post-game results ==")
# print("{}'s deck: {}".format(players[0], decks[players[0]]))
# print("{}'s deck: {}".format(players[1], decks[players[1]]))


print("winner is ", winner)
num_cards = len(decks[winner])

score = 0
for c in range(num_cards):
    print("+ {} * {}".format(decks[winner][c], (num_cards - c)))
    score += decks[winner][c] * (num_cards - c)
print("= {}".format(score))
