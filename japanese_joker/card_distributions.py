import random
from game_setup import GameSetup
from players import user_names
from total_cards_generator import total_cards_generator


# Distributes first three cards to each player
def three_card_distribution(total_cards, trump_card_chooser, card_distributor):
    players_and_their_cards = {f"{trump_card_chooser}": [],
                               f"{card_distributor}": []}
    for i in range(3):
        players_and_their_cards[trump_card_chooser].append(random.choice(total_cards))
        total_cards.remove(players_and_their_cards[trump_card_chooser][i])
        players_and_their_cards[card_distributor].append(random.choice(total_cards))
        total_cards.remove(players_and_their_cards[card_distributor][i])
    return players_and_their_cards, total_cards


# Distributes cards for each player on the field
def field_card_distribution(remaining_cards_30, trump_card_chooser, card_distributor):
    field_cards = {f"{trump_card_chooser}": {
                                            "face_down": [], "face_up": []},
                   f"{card_distributor}": {
                                            "face_down": [], "face_up": []}
                   }
    for j in ["face_down", "face_up"]:
        for i in range(5):
            field_cards[trump_card_chooser][j].append(random.choice(remaining_cards_30))
            remaining_cards_30.remove(field_cards[trump_card_chooser][j][i])
            field_cards[card_distributor][j].append(random.choice(remaining_cards_30))
            remaining_cards_30.remove(field_cards[card_distributor][j][i])
    remaining_cards_10 = remaining_cards_30
    return remaining_cards_10, field_cards


# Distributes the remaining cards to each player
def remaining_card_distribution(remaining_cards_10, players_and_their_cards):
    trump_card_chooser, card_distributor = map(lambda player: player, list(players_and_their_cards.keys()))
    while len(remaining_cards_10) != 0:
        players_and_their_cards[trump_card_chooser].append(random.choice(remaining_cards_10))
        remaining_cards_10.remove(players_and_their_cards[trump_card_chooser][-1])
        players_and_their_cards[card_distributor].append(random.choice(remaining_cards_10))
        remaining_cards_10.remove(players_and_their_cards[card_distributor][-1])
    return players_and_their_cards


def main():
    player_names = user_names()
    total_cards = list(total_cards_generator().keys())
    gameplay = GameSetup(player_names, total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    first_three_cards, remaining_30_cards = three_card_distribution(total_cards, card_distributor_player, trump_card_chooser_player)
    print(first_three_cards)
    print(len(remaining_30_cards))
    print(remaining_30_cards)
    remaining_10_cards, field_cards = field_card_distribution(remaining_30_cards, trump_card_chooser_player, card_distributor_player)
    print(remaining_10_cards)
    print(field_cards)
    print(remaining_card_distribution(remaining_10_cards, first_three_cards))


if __name__ == "__main__":
    main()
