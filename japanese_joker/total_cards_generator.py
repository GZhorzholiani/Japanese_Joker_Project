# Reads .json file, Generates Total Cards and returns their dict
import json


def total_cards_generator():
    try:
        with open("total_cards.json", "r") as file:
            total_cards = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("You have entered a wrong file")
    return total_cards["total_cards"]


def main():
    total_cards = list(total_cards_generator().keys())
    total_cards_and_ranks = total_cards_generator()
    #total_cards.remove("RJoker")
    #total_cards.remove("BJoker")
    print(total_cards)
    print(len(total_cards))
    print(total_cards_and_ranks)


if __name__ == "__main__":
    main()
