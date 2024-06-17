from deck_visualization import create_visualized_deck_dict, card_to_visualized_card
visualized_deck = create_visualized_deck_dict()


class CardToPlay:
    def __init__(self, player_name, players_final_cards_in_hands, field_cards, available_cards_to_play=None):
        self.player_name = player_name
        self.players_final_cards_in_hands = players_final_cards_in_hands
        self.field_cards = field_cards
        self.available_cards_to_play = available_cards_to_play

    @property
    def player_name(self):
        return self._player_name

    @player_name.setter
    def player_name(self, value):
        self._player_name = value

    @property
    def players_final_cards_in_hands(self):
        return self._players_final_cards_in_hands

    @players_final_cards_in_hands.setter
    def players_final_cards_in_hands(self, value):
        self._players_final_cards_in_hands = value

    @property
    def field_cards(self):
        return self._field_cards

    @field_cards.setter
    def field_cards(self, value):
        self._field_cards = value

    @property
    def available_cards_to_play(self):
        return self._available_cards_to_play

    @available_cards_to_play.setter
    def available_cards_to_play(self, value):
        self._available_cards_to_play = value

    def any_card_to_play(self):
        card_to_play_from_hand = {}
        card_to_play_from_field = {}
        card_counter_hand = 1
        while card_counter_hand <= len(self.players_final_cards_in_hands[self.player_name]):
            card_to_play_from_hand[f"{card_counter_hand}"] = self.players_final_cards_in_hands[self.player_name][card_counter_hand - 1]
            card_counter_hand += 1
        card_counter_field = 1
        while card_counter_field <= len(self.field_cards[self.player_name]['face_up']):
            card_to_play_from_field[f"{card_counter_hand}"] = self.field_cards[self.player_name]['face_up'][card_counter_field - 1]
            card_counter_hand += 1
            card_counter_field += 1
        playable_cards_with_numbers_hand = {}
        playable_cards_with_numbers_field = {}
        for number, card in card_to_play_from_hand.items():
            playable_cards_with_numbers_hand[number] = card_to_visualized_card([card], visualized_deck)[0]
        for number, card in card_to_play_from_field.items():
            playable_cards_with_numbers_field[number] = card_to_visualized_card([card], visualized_deck)[0]
        print(f"{'*' * 50}\n"
              f"{self.player_name}, it's your turn to play!\n"
              f"Cards in your hand are: {' '.join(card_to_visualized_card(self.players_final_cards_in_hands[self.player_name], visualized_deck))}\n"
              f"Available cards on the field are: {' '.join(card_to_visualized_card(self.field_cards[self.player_name]['face_up'], visualized_deck))}")
        while True:
            player_input_card_number = input(f"Please, choose a number associated with a card to play:\n"
                                             f"{', '.join([f'{key} - {value}' for key, value in playable_cards_with_numbers_hand.items()])}\n"
                                             f"{', '.join([f'{key} - {value}' for key, value in playable_cards_with_numbers_field.items()])} : ")
            if player_input_card_number in card_to_play_from_hand.keys():
                card_to_play = card_to_play_from_hand[player_input_card_number]
                print(f"{'*' * 50}")
                break
            if player_input_card_number in card_to_play_from_field.keys():
                card_to_play = card_to_play_from_field[player_input_card_number]
                print(f"{'*' * 50}")
                break
            print(f"{'*' * 50}")
            print("You have chosen a wrong card, Please choose again!")
        if card_to_play in self.players_final_cards_in_hands[self.player_name]:
            self.players_final_cards_in_hands[self.player_name].remove(card_to_play)
        elif card_to_play in self.field_cards[self.player_name]['face_up']:
            self.remove_played_card_from_the_field(card_to_play)
        return card_to_play

    def no_requested_card(self):
        card_to_play = self.available_card_to_play_with_visuals()
        if card_to_play in self.players_final_cards_in_hands[self.player_name] and card_to_play in self.available_cards_to_play:
            self.players_final_cards_in_hands[self.player_name].remove(card_to_play)
            print(f"{'*' * 50}")
        elif card_to_play in self.field_cards[self.player_name]['face_up'] and card_to_play in self.available_cards_to_play:
            self.remove_played_card_from_the_field(card_to_play)
            print(f"{'*' * 50}")
        return card_to_play

    def joker_action_request_card(self):
        card_to_play = self.available_card_to_play_with_visuals()
        if card_to_play in self.available_cards_to_play:
            if card_to_play in self.players_final_cards_in_hands[self.player_name]:
                self.players_final_cards_in_hands[self.player_name].remove(card_to_play)
                print(f"{'*' * 50}")
            elif card_to_play in ("BJOKER", "RJOKER") and card_to_play in self.field_cards[self.player_name]['face_up']:
                self.remove_played_card_from_the_field(card_to_play)
                print(f"{'*' * 50}")
        return card_to_play

    def add_joker_if_available(self):
        if "BJOKER" in self.players_final_cards_in_hands[self.player_name] + self.field_cards[self.player_name]["face_up"]:
            self.available_cards_to_play.append("BJOKER")
        if "RJOKER" in self.players_final_cards_in_hands[self.player_name] + self.field_cards[self.player_name]["face_up"]:
            self.available_cards_to_play.append("RJOKER")

    def remove_played_card_from_the_field(self, card_to_play):
        card_to_play_index = self.field_cards[self.player_name]['face_up'].index(card_to_play)
        self.field_cards[self.player_name]['face_up'].remove(card_to_play)
        self.players_final_cards_in_hands[self.player_name].append(self.field_cards[self.player_name]['face_down'][card_to_play_index])
        self.field_cards[self.player_name]['face_down'].remove(self.field_cards[self.player_name]['face_down'][card_to_play_index])

    def available_card_to_play_with_visuals(self):
        available_card_to_play = {}
        available_card_counter = 1
        while available_card_counter <= len(self.available_cards_to_play):
            available_card_to_play[f"{available_card_counter}"] = self.available_cards_to_play[
                available_card_counter - 1]
            available_card_counter += 1
        available_card_to_play_with_visuals = {}
        for number, card in available_card_to_play.items():
            available_card_to_play_with_visuals[number] = card_to_visualized_card([card], visualized_deck)[0]
        print(f"{'*' * 50}\n"
              f"{self.player_name}, it's your turn to play!\n"
              f"Cards in your hand are: {' '.join(card_to_visualized_card(self.players_final_cards_in_hands[self.player_name], visualized_deck))}\n"
              f"Cards on the field are: {' '.join(card_to_visualized_card(self.field_cards[self.player_name]['face_up'], visualized_deck))}\n"
              f"But you have to play from the following: {' '.join(card_to_visualized_card(self.available_cards_to_play, visualized_deck))}")
        while True:
            player_input_card_number = input(f"Please, choose a number associated with a card to play:\n"
                                             f"{', '.join([f'{key} - {value}' for key, value in available_card_to_play_with_visuals.items()])} : ")
            if player_input_card_number in available_card_to_play.keys():
                card_to_play = available_card_to_play[player_input_card_number]
                print(f"{'*' * 50}")
                break
            print(f"{'*' * 50}")
            print("You have chosen a wrong card, Please choose again!")
        return card_to_play
