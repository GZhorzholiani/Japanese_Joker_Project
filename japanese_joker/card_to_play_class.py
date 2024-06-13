

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
        while True:
            card_to_play = input(f"{'*' * 50}\n"
                                 f"{self.player_name}, it's your turn to play!\n"
                                 f"Cards in your hand are: {self.players_final_cards_in_hands[self.player_name]}\n"
                                 f"Available cards on the field are: {self.field_cards[self.player_name]['face_up']}\n"
                                 f"Please, choose a card to play: ").upper().strip()
            if card_to_play in self.players_final_cards_in_hands[self.player_name]:
                self.players_final_cards_in_hands[self.player_name].remove(card_to_play)
                print(f"{'*' * 50}")
                break
            elif card_to_play in self.field_cards[self.player_name]['face_up']:
                self.remove_played_card_from_the_field(card_to_play)
                print(f"{'*' * 50}")
                break
            print(f"{'*' * 50}")
            print("You have chosen a wrong card, Please choose again!")
        return card_to_play

    def no_requested_card(self):
        while True:
            card_to_play = input(f"{'*' * 50}\n"
                                 f"{self.player_name}, it's your turn to play!\n"
                                 f"Cards in your hand are: {self.players_final_cards_in_hands[self.player_name]}\n"
                                 f"Cards on the field are: {self.field_cards[self.player_name]['face_up']}\n"
                                 f"But you have to play from the following: {self.available_cards_to_play}\n"
                                 f"Please, choose a card to play: ").upper().strip()
            if card_to_play in self.players_final_cards_in_hands[self.player_name] and card_to_play in self.available_cards_to_play:
                self.players_final_cards_in_hands[self.player_name].remove(card_to_play)
                print(f"{'*' * 50}")
                break
            elif card_to_play in self.field_cards[self.player_name]['face_up'] and card_to_play in self.available_cards_to_play:
                self.remove_played_card_from_the_field(card_to_play)
                print(f"{'*' * 50}")
                break
            print(f"{'*' * 50}")
            print("You have chosen a wrong card, Please choose again!")
        return card_to_play

    def joker_action_request_card(self):
        while True:
            card_to_play = input(f"{'*' * 50}\n"
                                 f"{self.player_name}, it's your turn to play!\n"
                                 f"Cards in your hand are: {self.players_final_cards_in_hands[self.player_name]}\n"
                                 f"Cards on the field are: {self.field_cards[self.player_name]['face_up']}\n"
                                 f"But you have to play from the following: {self.available_cards_to_play}\n"
                                 f"Please, choose a card to play: ").upper().strip()
            if card_to_play in self.available_cards_to_play:
                self.players_final_cards_in_hands[self.player_name].remove(card_to_play)
                print(f"{'*' * 50}")
                break
            print(f"{'*' * 50}")
            print("You have chosen a wrong card, Please choose again!")
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
