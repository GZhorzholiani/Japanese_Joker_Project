# Reads .json file, Generates Total Cards and returns their list
import json


def total_cards_generator():
    try:
        with open("total_cards.json", "r") as file:
            total_cards = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError("You have entered a wrong file")
    return total_cards["total_cards"]


def main():
    total_cards = total_cards_generator()
    total_cards.remove("Joker")
    total_cards.remove("Joker")
    print(total_cards)
    print(len(total_cards))


if __name__ == "__main__":
    main()
