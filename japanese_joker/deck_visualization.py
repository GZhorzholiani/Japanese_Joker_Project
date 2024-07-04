from itertools import product


def create_visualized_deck():
    """
    Creates a deck for visualizing
    """
    suits = ['C', 'S', 'H', 'D']
    ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = ["{}{}".format(rank, suit) for rank, suit in product(ranks, suits)]
    deck.remove(deck[0])
    deck.remove(deck[0])
    deck.append('JR')
    deck.append('JB')
    return deck


def format_card(card):
    """
    Formats cards with Unicode specific meanings in order to get visual effects
    """
    suit_symbols = {
        "C": chr(9827),
        "S": chr(9824),
        "H": chr(9829),
        "D": chr(9830),
        "JR": "☆",
        "JB": "★"
    }
    red = '\033[31m'
    black = '\033[30m'
    background_white = '\033[107m'
    reset = '\033[0m'
    if card[-1] == "H" or card[-1] == "D" or card == "JR":
        color = red
    else:
        color = black
    if card[-1] in suit_symbols:
        suit_symbol = suit_symbols[card[-1]]
        formatted_card = f"{card[:-1]}{suit_symbol}"
    elif card in suit_symbols:
        suit_symbol = suit_symbols[card]
        formatted_card = f"{card[:-1]}{suit_symbol}"
    else:
        formatted_card = card
    formatted_card = f"{background_white}{color}{formatted_card}{reset}"
    return formatted_card


def get_formatted_deck(deck):
    """
    Returns fully formatted deck
    """
    return [format_card(card) for card in deck]


def create_visualized_deck_dict():
    """
    Creates visualized deck dictionary
    """
    visualized_deck = get_formatted_deck(create_visualized_deck())
    visualized_deck_dict = {"RJOKER": visualized_deck[34], "BJOKER": visualized_deck[35], "H6": visualized_deck[0], "D6": visualized_deck[1]}
    counter = 7
    card_meaning = counter
    card_index = 2
    while True:
        for j in ["C", "S", "H", "D"]:
            visualized_deck_dict[f"{j}{card_meaning}"] = visualized_deck[card_index]
            card_index += 1
        if counter < 10:
            counter += 1
            card_meaning += 1
        elif counter == 10:
            counter += 1
            card_meaning = "J"
        elif counter == 11:
            counter += 1
            card_meaning = "Q"
        elif counter == 12:
            counter += 1
            card_meaning = "K"
        elif counter == 13:
            counter += 1
            card_meaning = "A"
        elif counter == 14:
            break
    return visualized_deck_dict


def card_to_visualized_card(user_cards: list, visualized_deck_dict: dict) -> list:
    """
    Changes a card code (CA - Ace of Clubs) to code, which later will be printed as an actual card
    """
    visualized_list_of_cards = []
    for i in user_cards:
        visualized_list_of_cards.append(visualized_deck_dict.get(i))
    return visualized_list_of_cards


def main():
    visualized_deck_dict = create_visualized_deck_dict()
    print(visualized_deck_dict)
    print("\x1b[107m\x1b[31m♥\x1b[0m")
    for i in visualized_deck_dict.values():
        print(len(i), i)


if __name__ == "__main__":
    main()
