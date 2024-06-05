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
    a = total_cards_generator()
    a.remove("Joker")
    a.remove("Joker")
    print(a)
    print(len(a))


if __name__ == "__main__":
    main()
