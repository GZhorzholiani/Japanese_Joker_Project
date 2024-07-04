from players import user_names
from total_cards_generator import total_cards_generator
from game_setup import GameSetup
from card_distributions import three_card_distribution, field_card_distribution, remaining_card_distribution
from playing_game import round_winner_calculator
from deck_visualization import create_visualized_deck_dict, card_to_visualized_card

ROUND = 8


def main():
    global ROUND
    visualized_deck = create_visualized_deck_dict()
    print(f"{'*' * 64}\n"
          f"Game instructions: Jokers are represented as follow: {card_to_visualized_card(['RJOKER'], visualized_deck)[0]}"
          f" and {card_to_visualized_card(['BJOKER'], visualized_deck)[0]}")
    print("*" * 64)
    player_names = user_names()
    player_one = player_names[0]
    player_two = player_names[1]
    total_game_score = {f"{player_one}": 0, f"{player_two}": 0}
    round_counter = 1
    while True:
        print("*" * 50)
        print(f"Round {round_counter}, LETS GO!")
        player_names = [player_one, player_two]
        total_cards = list(total_cards_generator().keys())
        gameplay = GameSetup(player_names, total_cards)
        card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
        print("*" * 50)
        print(f"Card Distributor: {card_distributor_player}")
        print(f"Trump Card Chooser: {trump_card_chooser_player}")
        print("*" * 50)
        first_three_cards, remaining_cards_30 = three_card_distribution(total_cards, trump_card_chooser_player, card_distributor_player)
        print(f"{trump_card_chooser_player}, your first three cards: {' '.join(card_to_visualized_card(first_three_cards[trump_card_chooser_player], visualized_deck))}")
        print("*" * 50)
        trump_card, card_suits, trump_card_visual = gameplay.trump_card(trump_card_chooser_player)
        print("Trump Card is -", f"{trump_card_visual[trump_card]}" if trump_card != "NONE" else "None")
        total_cards_with_trump = gameplay.trump_card_effect(total_cards_generator(), trump_card)
        remaining_10_cards, field_cards = field_card_distribution(remaining_cards_30, trump_card_chooser_player, card_distributor_player)
        players_final_cards_in_hands = remaining_card_distribution(remaining_10_cards, first_three_cards)
        round_result = round_winner_calculator(field_cards, players_final_cards_in_hands, total_cards_with_trump, trump_card, card_suits)
        if round_result[trump_card_chooser_player] > round_result[card_distributor_player]:
            print(f"This round goes to {trump_card_chooser_player}")
            if trump_card_chooser_player == player_one:
                total_game_score[f"{player_one}"] += 1
            else:
                total_game_score[f"{player_two}"] += 1
        elif round_result[trump_card_chooser_player] < round_result[card_distributor_player]:
            print(f"This round goes to {card_distributor_player}")
            if card_distributor_player == player_one:
                total_game_score[f"{player_one}"] += 1
            else:
                total_game_score[f"{player_two}"] += 1
        else:
            print("This round is a Tie!")
        round_counter += 1
        print("*" * 50)
        print(f"Total Game Score: {', '.join([f'{key} - {value}' for key, value in total_game_score.items()])}")
        if total_game_score[f"{player_one}"] == ROUND:
            break
        elif total_game_score[f"{player_two}"] == ROUND:
            break
    print("*" * 50)
    if total_game_score[f"{player_one}"] == ROUND:
        print(f"{player_one} has won the match!")
    elif total_game_score[f"{player_two}"] == ROUND:
        print(f"{player_two} has won the match!")


if __name__ == "__main__":
    main()
