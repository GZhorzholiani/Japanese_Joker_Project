from players import user_names
from total_cards_generator import total_cards_generator
from game_setup import GameSetup
from card_distributions import three_card_distribution, field_card_distribution, remaining_card_distribution


def player_turn(player_name, players_final_cards_in_hands, field_cards):
    while True:
        card_to_play = input(f"{'*' * 50}\n"
                             f"{player_name}, it's your turn to play!\n"
                             f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                             f"Available cards on the field are: {field_cards[player_name]['face_up']}\n"
                             f"Please, choose play a card: ").upper().strip()
        if card_to_play in players_final_cards_in_hands[player_name]:
            players_final_cards_in_hands[player_name].remove(card_to_play)
            break
        elif card_to_play in field_cards[player_name]['face_up']:
            card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
            field_cards[player_name]['face_up'].remove(card_to_play)
            players_final_cards_in_hands[player_name].append(field_cards[player_name]['face_down'][card_to_play_index])
            field_cards[player_name]['face_down'].remove(field_cards[player_name]['face_down'][card_to_play_index])
            break
    print(f"{'*' * 50}\n"
          f"{player_name} has played - {card_to_play}")
    return card_to_play


def round_winner_calculator(field_cards, players_final_cards_in_hands, total_cards_with_trump):
    first_to_play = list(players_final_cards_in_hands.keys())[0]
    second_to_play = list(players_final_cards_in_hands.keys())[1]
    player_scores = {f"{first_to_play}": 0, f"{second_to_play}": 0}

    while sum(list(player_scores.values())) <= 18:
        first_card_to_play = player_turn(first_to_play, players_final_cards_in_hands, field_cards)
        second_card_to_play = player_turn(second_to_play, players_final_cards_in_hands, field_cards)
        if total_cards_with_trump[first_card_to_play] > total_cards_with_trump[second_card_to_play]:
            list(player_scores.values())[0] += 1
        elif total_cards_with_trump[first_card_to_play] < total_cards_with_trump[second_card_to_play]:
            list(player_scores.values())[1]] += 1


    # if list(player_scores.values())[0] > list(player_scores.values())[1]:
    #     return list(player_scores.keys())[0]
    # elif list(player_scores.values())[0] < list(player_scores.values())[1]:
    #     return list(player_scores.keys())[1]
    # else:
    #     return None


def main():
    player_names = user_names()
    total_cards = list(total_cards_generator().keys())
    gameplay = GameSetup(player_names, total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    first_three_cards, remaining_cards_30 = three_card_distribution(total_cards, trump_card_chooser_player, card_distributor_player)
    trump_card = gameplay.trump_card(trump_card_chooser_player)
    total_cards_with_trump = gameplay.trump_card_effect(total_cards_generator(), trump_card)
    remaining_10_cards, field_cards = field_card_distribution(remaining_cards_30, trump_card_chooser_player, card_distributor_player)
    players_final_cards_in_hands = remaining_card_distribution(remaining_10_cards, first_three_cards)
    test = round_winner_calculator(field_cards, players_final_cards_in_hands, total_cards_with_trump)
    print(test)


if __name__ == "__main__":
    main()
