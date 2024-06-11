from players import user_names
from total_cards_generator import total_cards_generator
from game_setup import GameSetup
from card_distributions import three_card_distribution, field_card_distribution, remaining_card_distribution


def player_turn(player_name, players_final_cards_in_hands, field_cards, trump_card, card_suits, previous_player_card=None, joker_action=None, total_cards_with_trump=None):
    if previous_player_card is None:
        while True:
            card_to_play = input(f"{'*' * 50}\n"
                                 f"{player_name}, it's your turn to play!\n"
                                 f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                 f"Available cards on the field are: {field_cards[player_name]['face_up']}\n"
                                 f"Please, choose a card to play: ").upper().strip()
            if card_to_play in players_final_cards_in_hands[player_name]:
                players_final_cards_in_hands[player_name].remove(card_to_play)
                break
            elif card_to_play in field_cards[player_name]['face_up']:
                card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                field_cards[player_name]['face_up'].remove(card_to_play)
                players_final_cards_in_hands[player_name].append(field_cards[player_name]['face_down'][card_to_play_index])
                field_cards[player_name]['face_down'].remove(field_cards[player_name]['face_down'][card_to_play_index])
                break
            print(f"{'*' * 50}")
            print("You have chosen a wrong card, Please choose again!")
        if card_to_play in ("BJOKER", "RJOKER"):
            while True:
                if trump_card == "NONE":
                    joker_action = input(f"Which highest card do you request? - {card_suits}: ").upper().strip()
                    if joker_action in card_suits:
                        break
                else:
                    joker_action = input(f"Which highest card do you request?: {card_suits}, trump - {trump_card}: ").upper().strip()
                    if joker_action in ["S", "D", "C", "H"]:
                        break
        print(f"{'*' * 50}")
        if joker_action is None:
            print(f"{player_name} has played - {card_to_play}")
        else:
            print(f"{player_name} has played - {card_to_play} and requested Highest - {joker_action}")
        return card_to_play, joker_action
    else:
        available_cards_to_play = []
        if previous_player_card in ("BJOKER", "RJOKER"):
            for joker in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                if joker == "BJOKER":
                    available_cards_to_play.append(joker)
                elif joker == "RJOKER":
                    available_cards_to_play.append(joker)
            joker_action_request = {}
            for playable_card in players_final_cards_in_hands[player_name]:
                if playable_card[0] == joker_action:
                    joker_action_request[playable_card] = 0
            if len(joker_action_request) == 0:
                if trump_card is None:
                    print("You dont have a requested card, you can play whatever you like!")
                    while True:
                        card_to_play = input(f"{'*' * 50}\n"
                                             f"{player_name}, it's your turn to play!\n"
                                             f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                             f"Available cards on the field are: {field_cards[player_name]['face_up']}\n"
                                             f"Please, choose a card to play: ").upper().strip()
                        if card_to_play in players_final_cards_in_hands[player_name]:
                            players_final_cards_in_hands[player_name].remove(card_to_play)
                            print(f"{'*' * 50}")
                            break
                        elif card_to_play in field_cards[player_name]['face_up']:
                            card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                            field_cards[player_name]['face_up'].remove(card_to_play)
                            players_final_cards_in_hands[player_name].append(field_cards[player_name]['face_down'][card_to_play_index])
                            field_cards[player_name]['face_down'].remove(field_cards[player_name]['face_down'][card_to_play_index])
                            print(f"{'*' * 50}")
                            break
                        print(f"{'*' * 50}")
                        print("You have chosen a wrong card, Please choose again!")
                    return card_to_play
                else:
                    available_cards_to_play = []
                    for card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                        if card[0] == trump_card:
                            available_cards_to_play.append(card)
                    if len(available_cards_to_play) == 0:
                        print("You dont have a requested card nor a trump card in your hand, so you can play whatever you like!")
                        while True:
                            card_to_play = input(f"{'*' * 50}\n"
                                                 f"{player_name}, it's your turn to play!\n"
                                                 f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                                 f"Available cards on the field are: {field_cards[player_name]['face_up']}\n"
                                                 f"Please, choose a card to play: ").upper().strip()
                            if card_to_play in players_final_cards_in_hands[player_name]:
                                players_final_cards_in_hands[player_name].remove(card_to_play)
                                print(f"{'*' * 50}")
                                break
                            elif card_to_play in field_cards[player_name]['face_up']:
                                card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                                field_cards[player_name]['face_up'].remove(card_to_play)
                                players_final_cards_in_hands[player_name].append(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                field_cards[player_name]['face_down'].remove(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                print(f"{'*' * 50}")
                                break
                            print(f"{'*' * 50}")
                            print("You have chosen a wrong card, Please choose again!")
                        if card_to_play[0] == trump_card:
                            card_to_play = "BJOKER"
                        return card_to_play
                    else:
                        for joker in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                            if joker == "BJOKER":
                                available_cards_to_play.append(joker)
                            elif joker == "RJOKER":
                                available_cards_to_play.append(joker)
                        print("You dont have a requested card but you have a trump card!")
                        while True:
                            card_to_play = input(f"{'*' * 50}\n"
                                                 f"{player_name}, it's your turn to play!\n"
                                                 f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                                 f"Cards on the field are: {field_cards[player_name]['face_up']}\n"
                                                 f"But you have to play from the following: {available_cards_to_play}\n"
                                                 f"Please, choose a card to play: ").upper().strip()
                            if card_to_play in players_final_cards_in_hands[player_name] and card_to_play in available_cards_to_play:
                                players_final_cards_in_hands[player_name].remove(card_to_play)
                                print(f"{'*' * 50}")
                                break
                            elif card_to_play in field_cards[player_name]['face_up'] and card_to_play in available_cards_to_play:
                                card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                                field_cards[player_name]['face_up'].remove(card_to_play)
                                players_final_cards_in_hands[player_name].append(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                field_cards[player_name]['face_down'].remove(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                print(f"{'*' * 50}")
                                break
                            print(f"{'*' * 50}")
                            print("You have chosen a wrong card, Please choose again!")
                        card_to_play = "BJOKER"
                        return card_to_play
            elif len(joker_action_request) == 1:
                available_cards_to_play.extend(joker_action_request.keys())
            else:
                for card in joker_action_request:
                    joker_action_request[card] += total_cards_with_trump.get(card, 0)
                available_cards_to_play.append(max(joker_action_request, key=joker_action_request.get))
            while True:
                card_to_play = input(f"{'*' * 50}\n"
                                     f"{player_name}, it's your turn to play!\n"
                                     f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                     f"Cards on the field are: {field_cards[player_name]['face_up']}\n"
                                     f"But you have to play from the following: {available_cards_to_play}\n"
                                     f"Please, choose a card to play: ").upper().strip()
                if card_to_play in available_cards_to_play:
                    players_final_cards_in_hands[player_name].remove(card_to_play)
                    print(f"{'*' * 50}")
                    break
                print(f"{'*' * 50}")
                print("You have chosen a wrong card, Please choose again!")
            return card_to_play
        elif previous_player_card[0] == trump_card:
            for playable_card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                if playable_card[0] == trump_card:
                    available_cards_to_play.append(playable_card)
            if len(available_cards_to_play) != 0:
                if "BJOKER" in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                    available_cards_to_play.append("BJOKER")
                if "RJOKER" in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                    available_cards_to_play.append("RJOKER")
                while True:
                    card_to_play = input(f"{'*' * 50}\n"
                                         f"{player_name}, it's your turn to play!\n"
                                         f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                         f"Cards on the field are: {field_cards[player_name]['face_up']}\n"
                                         f"But you have to play from the following: {available_cards_to_play}\n"
                                         f"Please, choose a card to play: ").upper().strip()
                    if card_to_play in players_final_cards_in_hands[player_name] and card_to_play in available_cards_to_play:
                        players_final_cards_in_hands[player_name].remove(card_to_play)
                        print(f"{'*' * 50}")
                        break
                    elif card_to_play in field_cards[player_name]['face_up'] and card_to_play in available_cards_to_play:
                        card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                        field_cards[player_name]['face_up'].remove(card_to_play)
                        players_final_cards_in_hands[player_name].append(field_cards[player_name]['face_down'][card_to_play_index])
                        field_cards[player_name]['face_down'].remove(field_cards[player_name]['face_down'][card_to_play_index])
                        print(f"{'*' * 50}")
                        break
                    print(f"{'*' * 50}")
                    print("You have chosen a wrong card, Please choose again!")
                return card_to_play
            else:
                print("You dont have a trump card to play, you can play whatever you like!")
                while True:
                    card_to_play = input(f"{'*' * 50}\n"
                                         f"{player_name}, it's your turn to play!\n"
                                         f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                         f"Available cards on the field are: {field_cards[player_name]['face_up']}\n"
                                         f"Please, choose a card to play: ").upper().strip()
                    if card_to_play in players_final_cards_in_hands[player_name]:
                        players_final_cards_in_hands[player_name].remove(card_to_play)
                        print(f"{'*' * 50}")
                        break
                    elif card_to_play in field_cards[player_name]['face_up']:
                        card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                        field_cards[player_name]['face_up'].remove(card_to_play)
                        players_final_cards_in_hands[player_name].append(
                            field_cards[player_name]['face_down'][card_to_play_index])
                        field_cards[player_name]['face_down'].remove(
                            field_cards[player_name]['face_down'][card_to_play_index])
                        print(f"{'*' * 50}")
                        break
                    print(f"{'*' * 50}")
                    print("You have chosen a wrong card, Please choose again!")
                return card_to_play
        else:
            for playable_card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                if playable_card[0] == previous_player_card[0]:
                    available_cards_to_play.append(playable_card)
            if len(available_cards_to_play) != 0:
                if "BJOKER" in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                    available_cards_to_play.append("BJOKER")
                if "RJOKER" in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                    available_cards_to_play.append("RJOKER")
                while True:
                    card_to_play = input(f"{'*' * 50}\n"
                                         f"{player_name}, it's your turn to play!\n"
                                         f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                         f"Cards on the field are: {field_cards[player_name]['face_up']}\n"
                                         f"But you have to play from the following: {available_cards_to_play}\n"
                                         f"Please, choose a card to play: ").upper().strip()
                    if card_to_play in players_final_cards_in_hands[player_name] and card_to_play in available_cards_to_play:
                        players_final_cards_in_hands[player_name].remove(card_to_play)
                        print(f"{'*' * 50}")
                        break
                    elif card_to_play in field_cards[player_name]['face_up'] and card_to_play in available_cards_to_play:
                        card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                        field_cards[player_name]['face_up'].remove(card_to_play)
                        players_final_cards_in_hands[player_name].append(field_cards[player_name]['face_down'][card_to_play_index])
                        field_cards[player_name]['face_down'].remove(field_cards[player_name]['face_down'][card_to_play_index])
                        print(f"{'*' * 50}")
                        break
                    print(f"{'*' * 50}")
                    print("You have chosen a wrong card, Please choose again!")
                return card_to_play
            else:
                if trump_card is not None:
                    available_cards_to_play = []
                    for card in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                        if card[0] == trump_card:
                            available_cards_to_play.append(card)
                    if len(available_cards_to_play) != 0:
                        for joker in players_final_cards_in_hands[player_name] + field_cards[player_name]["face_up"]:
                            if joker == "BJOKER":
                                available_cards_to_play.append(joker)
                            if joker == "RJOKER":
                                available_cards_to_play.append(joker)
                        print("You dont have a requested card but you have a trump card!")
                        while True:
                            card_to_play = input(f"{'*' * 50}\n"
                                                 f"{player_name}, it's your turn to play!\n"
                                                 f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                                 f"Cards on the field are: {field_cards[player_name]['face_up']}\n"
                                                 f"But you have to play from the following: {available_cards_to_play}\n"
                                                 f"Please, choose a card to play: ").upper().strip()
                            if card_to_play in players_final_cards_in_hands[player_name] and card_to_play in available_cards_to_play:
                                players_final_cards_in_hands[player_name].remove(card_to_play)
                                print(f"{'*' * 50}")
                                break
                            elif card_to_play in field_cards[player_name]['face_up'] and card_to_play in available_cards_to_play:
                                card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                                field_cards[player_name]['face_up'].remove(card_to_play)
                                players_final_cards_in_hands[player_name].append(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                field_cards[player_name]['face_down'].remove(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                print(f"{'*' * 50}")
                                break
                            print(f"{'*' * 50}")
                            print("You have chosen a wrong card, Please choose again!")
                        return card_to_play
                    else:
                        print(f"You dont have a {previous_player_card[0]} suit nor you have a trump card to play, you can play whatever you like!")
                        while True:
                            card_to_play = input(f"{'*' * 50}\n"
                                                 f"{player_name}, it's your turn to play!\n"
                                                 f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                                 f"Available cards on the field are: {field_cards[player_name]['face_up']}\n"
                                                 f"Please, choose a card to play: ").upper().strip()
                            if card_to_play in players_final_cards_in_hands[player_name]:
                                players_final_cards_in_hands[player_name].remove(card_to_play)
                                print(f"{'*' * 50}")
                                break
                            elif card_to_play in field_cards[player_name]['face_up']:
                                card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                                field_cards[player_name]['face_up'].remove(card_to_play)
                                players_final_cards_in_hands[player_name].append(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                field_cards[player_name]['face_down'].remove(
                                    field_cards[player_name]['face_down'][card_to_play_index])
                                print(f"{'*' * 50}")
                                break
                            print(f"{'*' * 50}")
                            print("You have chosen a wrong card, Please choose again!")
                        if card_to_play in ("BJOKER", "RJOKER"):
                            return card_to_play
                        else:
                            return None
                else:
                    print(f"You dont have {previous_player_card[0]} card to play, you can play whatever you like!")
                    while True:
                        card_to_play = input(f"{'*' * 50}\n"
                                             f"{player_name}, it's your turn to play!\n"
                                             f"Cards in your hand are: {players_final_cards_in_hands[player_name]}\n"
                                             f"Available cards on the field are: {field_cards[player_name]['face_up']}\n"
                                             f"Please, choose a card to play: ").upper().strip()
                        if card_to_play in players_final_cards_in_hands[player_name]:
                            players_final_cards_in_hands[player_name].remove(card_to_play)
                            print(f"{'*' * 50}")
                            break
                        elif card_to_play in field_cards[player_name]['face_up']:
                            card_to_play_index = field_cards[player_name]['face_up'].index(card_to_play)
                            field_cards[player_name]['face_up'].remove(card_to_play)
                            players_final_cards_in_hands[player_name].append(field_cards[player_name]['face_down'][card_to_play_index])
                            field_cards[player_name]['face_down'].remove(field_cards[player_name]['face_down'][card_to_play_index])
                            print(f"{'*' * 50}")
                            break
                        print(f"{'*' * 50}")
                        print("You have chosen a wrong card, Please choose again!")
                    if card_to_play in ("BJOKER", "RJOKER"):
                        return card_to_play
                    else:
                        return None


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
            starting_player = player_one
        elif total_cards_with_trump[player_one_card] > total_cards_with_trump[player_two_card]:
            player_scores[f"{player_one}"] += 1
            print(f"One point to - {player_one}")
            starting_player = player_one
        elif total_cards_with_trump[player_one_card] <= total_cards_with_trump[player_two_card]:
            player_scores[f"{player_two}"] += 1
            print(f"One point to - {player_two}")
            starting_player = player_two
    return player_scores


def main():
    player_names = user_names()
    total_cards = list(total_cards_generator().keys())
    gameplay = GameSetup(player_names, total_cards)
    card_distributor_player, trump_card_chooser_player = gameplay.card_distributor_and_trump_card_chooser()
    first_three_cards, remaining_cards_30 = three_card_distribution(total_cards, trump_card_chooser_player, card_distributor_player)
    print(first_three_cards)
    trump_card, card_suits = gameplay.trump_card(trump_card_chooser_player)
    total_cards_with_trump = gameplay.trump_card_effect(total_cards_generator(), trump_card)
    remaining_10_cards, field_cards = field_card_distribution(remaining_cards_30, trump_card_chooser_player, card_distributor_player)
    players_final_cards_in_hands = remaining_card_distribution(remaining_10_cards, first_three_cards)
    test = round_winner_calculator(field_cards, players_final_cards_in_hands, total_cards_with_trump, trump_card, card_suits)
    print(test)


if __name__ == "__main__":
    main()
