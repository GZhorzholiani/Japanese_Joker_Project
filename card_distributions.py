import random

from game_setup import GameSetup
from players import user_names
from total_cards_generator import total_cards_generator


def three_card_distribution(total_cards, card_distributor, trump_card_chooser):
    players_and_their_cards = {f"{card_distributor}": [],
                               f"{trump_card_chooser}": []}
    for i in range(3):
        players_and_their_cards[card_distributor].append(random.choice(total_cards))
        total_cards.remove(players_and_their_cards[card_distributor][i])
        players_and_their_cards[trump_card_chooser].append(random.choice(total_cards))
        total_cards.remove(players_and_their_cards[trump_card_chooser][i])
    return players_and_their_cards


#def

def main():
    player_names = user_names()
    total_cards = total_cards_generator()
    gameplay = GameSetup(player_names, total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    first_three_cards = three_card_distribution(total_cards, card_distributor_player, trump_card_chooser_player)
    print(first_three_cards)
    print(len(total_cards))
    print(total_cards)


if __name__ == "__main__":
    main()
