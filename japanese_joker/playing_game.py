from players import user_names
from total_cards_generator import total_cards_generator
from game_setup import GameSetup
from card_distributions import three_card_distribution, field_card_distribution, remaining_card_distribution
from card_to_play_class import CardToPlay
from deck_visualization import create_visualized_deck_dict, card_to_visualized_card
visualized_deck = create_visualized_deck_dict()


# Based on which player's turn it is, this function adds restrictions and provides user with available cards to play
def player_turn(player_name, players_final_cards_in_hands, field_cards, trump_card, card_suits, previous_player_card=None, joker_action=None, total_cards_with_trump=None):
    card_suit_visual = {"C": '\x1b[107m\x1b[30m♣\x1b[0m', "S": '\x1b[107m\x1b[30m♠\x1b[0m',
                        "H": '\x1b[107m\x1b[31m♥\x1b[0m', "D": '\x1b[107m\x1b[31m♦\x1b[0m'}
    if previous_player_card is None:
        player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards)
        card_to_play = player_action.any_card_to_play()
        if card_to_play in ("BJOKER", "RJOKER"):
            while True:
                try:
                    if trump_card == "NONE":
                        joker_action = input(f"Which highest card do you request? Type {card_suits[0]} for {card_suit_visual[card_suits[0]]}, "
                                             f"{card_suits[1]} for {card_suit_visual[card_suits[1]]}, "
                                             f"{card_suits[2]} for {card_suit_visual[card_suits[2]]}, "
                                             f"{card_suits[3]} for {card_suit_visual[card_suits[3]]}: ").upper().strip()
                        if joker_action in card_suits:
                            break
                    else:
                        joker_action = input(f"Which highest card do you request?: Type {card_suits[0]} for {card_suit_visual[card_suits[0]]}, "
                                             f"{card_suits[1]} for {card_suit_visual[card_suits[1]]}, "
                                             f"{card_suits[2]} for {card_suit_visual[card_suits[2]]}, "
                                             f"or a trump: {trump_card[0]} - {card_suit_visual[trump_card[0]]}: ").upper().strip()
                        if joker_action in ["C", "S", "H", "D"]:
                            break
                except ValueError:
                    print("Oops, something went wrong, please try again")
        if joker_action is None:
            print(f"{player_name} has played - {card_to_visualized_card([card_to_play], visualized_deck)[0]}")
        else:
            print(f"{player_name} has played - {card_to_visualized_card([card_to_play], visualized_deck)[0]} and requested Highest - {card_suit_visual[joker_action]}")
        return card_to_play, joker_action
    else:
        available_cards_to_play = []
        if previous_player_card in ("BJOKER", "RJOKER"):
            add_joker_if_possible = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
            add_joker_if_possible.add_joker_if_available()
            joker_action_request = {}
            for playable_card in players_final_cards_in_hands[player_name]:
                if playable_card[0] == joker_action:
                    joker_action_request[playable_card] = 0
            if len(joker_action_request) == 0:
                if trump_card == "NONE":
                    print(f"You dont have a requested card {card_suit_visual[joker_action]}, you can play whatever you like!")
                    player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards)
                    card_to_play = player_action.any_card_to_play()
                    return card_to_play
                else:
                    available_cards_to_play = []
                    for card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                        if card[0] == trump_card:
                            available_cards_to_play.append(card)
                    if len(available_cards_to_play) == 0:
                        print(f"You dont have a requested card {card_suit_visual[joker_action]}, nor a trump card {card_suit_visual[trump_card]} in your hand, so you can play whatever you like!"
                              if joker_action != trump_card else
                              f"You dont have a requested card {card_suit_visual[joker_action]} in your hand, you can play whatever you like!")
                        player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards)
                        card_to_play = player_action.any_card_to_play()
                        if card_to_play[0] == trump_card:
                            card_to_play = "BJOKER"
                        return card_to_play
                    else:
                        add_joker_if_possible = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                        add_joker_if_possible.add_joker_if_available()
                        print(f"You dont have a requested card {card_suit_visual[joker_action]} in your hand, but you have a trump card {card_suit_visual[trump_card]}!")
                        player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                        player_action.no_requested_card()
                        card_to_play = "BJOKER"
                        return card_to_play
            elif len(joker_action_request) == 1:
                available_cards_to_play.extend(joker_action_request.keys())
            else:
                for card in joker_action_request:
                    joker_action_request[card] += total_cards_with_trump.get(card, 0)
                available_cards_to_play.append(max(joker_action_request, key=joker_action_request.get))
            player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
            card_to_play = player_action.joker_action_request_card()
            return card_to_play
        elif previous_player_card[0] == trump_card:
            for playable_card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                if playable_card[0] == trump_card:
                    available_cards_to_play.append(playable_card)
            if len(available_cards_to_play) != 0:
                add_joker_if_possible = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                add_joker_if_possible.add_joker_if_available()
                player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                card_to_play = player_action.no_requested_card()
                return card_to_play
            else:
                print(f"You dont have a trump card {card_suit_visual[trump_card]} to play, you can play whatever you like!")
                player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards)
                card_to_play = player_action.any_card_to_play()
                return card_to_play
        else:
            for playable_card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                if playable_card[0] == previous_player_card[0]:
                    available_cards_to_play.append(playable_card)
            if len(available_cards_to_play) != 0:
                add_joker_if_possible = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                add_joker_if_possible.add_joker_if_available()
                player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                card_to_play = player_action.no_requested_card()
                return card_to_play
            else:
                if trump_card != "NONE":
                    available_cards_to_play = []
                    for card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                        if card[0] == trump_card:
                            available_cards_to_play.append(card)
                    if len(available_cards_to_play) != 0:
                        add_joker_if_possible = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                        add_joker_if_possible.add_joker_if_available()
                        print(f"You dont have a requested card {card_suit_visual[previous_player_card[0]]} but you have a trump card {card_suit_visual[trump_card]}!")
                        player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards, available_cards_to_play)
                        card_to_play = player_action.no_requested_card()
                        return card_to_play
                    else:
                        print(f"You dont have a {card_suit_visual[previous_player_card[0]]} suit nor you have a trump card {card_suit_visual[trump_card]} to play, you can play whatever you like!")
                        player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards)
                        card_to_play = player_action.any_card_to_play()
                        if card_to_play in ("BJOKER", "RJOKER"):
                            return card_to_play
                        else:
                            return None
                else:
                    print(f"You dont have {card_suit_visual[previous_player_card[0]]} card to play, you can play whatever you like!")
                    player_action = CardToPlay(player_name, players_final_cards_in_hands, field_cards)
                    card_to_play = player_action.any_card_to_play()
                    if card_to_play in ("BJOKER", "RJOKER"):
                        return card_to_play
                    else:
                        return None


# Plays a full round of game where max score is 18
def round_winner_calculator(field_cards, players_final_cards_in_hands, total_cards_with_trump, trump_card, card_suits):
    player_one = list(players_final_cards_in_hands.keys())[0]
    player_two = list(players_final_cards_in_hands.keys())[1]
    starting_player = player_one
    player_scores = {f"{player_one}": 0, f"{player_two}": 0}
    while sum([player_scores[f"{player_one}"], player_scores[f"{player_two}"]]) < 18:
        if starting_player == player_one:
            player_one_card, joker_action = player_turn(player_one, players_final_cards_in_hands, field_cards, trump_card, card_suits)
            player_two_card = player_turn(player_two, players_final_cards_in_hands, field_cards, trump_card, card_suits, player_one_card, joker_action, total_cards_with_trump)
        else:
            player_two_card, joker_action = player_turn(player_two, players_final_cards_in_hands, field_cards, trump_card, card_suits)
            player_one_card = player_turn(player_one, players_final_cards_in_hands, field_cards, trump_card, card_suits, player_two_card, joker_action, total_cards_with_trump)
        if player_two_card is None:
            player_scores[f"{player_one}"] += 1
            print(f"One point to - {player_one}")
            print(f"Total score for this round : {player_one} - {player_scores[player_one]}. {player_two} - {player_scores[player_two]}")
            starting_player = player_one
        elif player_one_card is None:
            player_scores[f"{player_two}"] += 1
            print(f"One point to - {player_two}")
            print(f"Total score for this round : {player_one} - {player_scores[player_one]}. {player_two} - {player_scores[player_two]}")
            starting_player = player_two
        elif total_cards_with_trump[player_one_card] > total_cards_with_trump[player_two_card]:
            player_scores[f"{player_one}"] += 1
            print(f"One point to - {player_one}")
            print(f"Total score for this round : {player_one} - {player_scores[player_one]}. {player_two} - {player_scores[player_two]}")
            starting_player = player_one
        elif total_cards_with_trump[player_one_card] <= total_cards_with_trump[player_two_card]:
            player_scores[f"{player_two}"] += 1
            print(f"One point to - {player_two}")
            print(f"Total score for this round : {player_one} - {player_scores[player_one]}. {player_two} - {player_scores[player_two]}")
            starting_player = player_two
    return player_scores


def main():
    player_names = user_names()
    total_cards = list(total_cards_generator().keys())
    gameplay = GameSetup(player_names, total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    first_three_cards, remaining_cards_30 = three_card_distribution(total_cards, trump_card_chooser_player, card_distributor_player)
    print(first_three_cards)
    trump_card, card_suits, trump_card_visual = gameplay.trump_card(trump_card_chooser_player)
    total_cards_with_trump = gameplay.trump_card_effect(total_cards_generator(), trump_card)
    remaining_10_cards, field_cards = field_card_distribution(remaining_cards_30, trump_card_chooser_player, card_distributor_player)
    players_final_cards_in_hands = remaining_card_distribution(remaining_10_cards, first_three_cards)
    test = round_winner_calculator(field_cards, players_final_cards_in_hands, total_cards_with_trump, trump_card, card_suits)
    print(test)


if __name__ == "__main__":
    main()
