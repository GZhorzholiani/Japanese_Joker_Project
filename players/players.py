# Asks users for their player nicknames and returns list of 2 players
def user_names():
    all_players = []
    counter = 1
    while counter <= 2:
        while True:
            player_name = input(f"Please enter player {counter} name: ")
            if player_name in all_players:
                print(f"Name {player_name} already taken, please enter a different name!")
                continue
            else:
                all_players.append(player_name)
                counter += 1
                break
    return all_players


def main():
    a = user_names()
    print(a)


if __name__ == "__main__":
    main()
