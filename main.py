from players import user_names
from total_cards_generator import total_cards_generator
from game_setup import GameSetup
from card_distributions import three_card_distribution, field_card_distribution, remaining_card_distribution


def main():
    player_names = user_names()
    total_cards = list(total_cards_generator().keys())
    gameplay = GameSetup(player_names, total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    print("*" * 50)
    print(f"Card Distributor: {card_distributor_player}")
    print(f"Trump Card Chooser: {trump_card_chooser_player}")
    print("*" * 50)
    first_three_cards, remaining_cards_30 = three_card_distribution(total_cards, trump_card_chooser_player, card_distributor_player)
    print(first_three_cards)
    print("*" * 50)
    trump_card, card_suits = gameplay.trump_card(trump_card_chooser_player)
    print(f"Trump Card is - {trump_card}")
    print("*" * 50)
    total_cards_with_trump = gameplay.trump_card_effect(total_cards_generator(), trump_card)
    remaining_10_cards, field_cards = field_card_distribution(remaining_cards_30, trump_card_chooser_player, card_distributor_player)
    print(field_cards)
    print("*" * 50)
    players_final_cards_in_hands = remaining_card_distribution(remaining_10_cards, first_three_cards)
    print(players_final_cards_in_hands)


if __name__ == "__main__":
    main()