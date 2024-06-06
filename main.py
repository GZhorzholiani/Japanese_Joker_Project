from players import user_names
from total_cards_generator import total_cards_generator
from game_setup import GameSetup
from card_distributions import three_card_distribution


def main():
    player_names = user_names()
    total_cards = total_cards_generator()
    gameplay = GameSetup(player_names, total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    print("*" * 50)
    print(f"Card Distributor: {card_distributor_player}")
    print(f"Trump Card Chooser: {trump_card_chooser_player}")
    print("*" * 50)
    first_three_cards = three_card_distribution(total_cards, card_distributor_player, trump_card_chooser_player)
    print(first_three_cards)
    print("*" * 50)
    trump_card = gameplay.trump_card(trump_card_chooser_player)
    print(f"Trump Card is - {trump_card}")
    print("*" * 50)


if __name__ == "__main__":
    main()
