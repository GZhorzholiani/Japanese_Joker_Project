# Japanese Joker
Two player card game

### Card Distribution Rules
* Random player is chosen as a card distributor.
* Card Distributor player deals three cards to each player.
* Other player is considered as a Trump Card Choosing player who chooses a trump card.
* Trump Card can be Clubs, Spaces, Hearts, Diamonds or None of the listed.
* After choosing a trump card, card distributor player distributes five cards facing down to each player in front of them on the board.
* After distributing face down cards, he/she continues to distribute five cards facing up to each player in front of them on the board on top of previously put face down cards.
* Card Distributor player distributes the remaining cards to each players hands.

### Player Turns
* Trump card chooser begins the turn.
* Card Distributor player has to answer previous players chosen card.
* Player, who's card has more power scores one point, now it is his turn to play first.
* After all 36 cards are played, if either player has more than 9 score he/she wins the round. If both players scored 9 points, it is a tie.
* The game lasts until either player has won 8 rounds.

### Game Restrictions
* If a player who begins a turn plays a joker, he/she may request the highest card of any suit from the second players hand. Second player must play the requested card if they have it, or they can play a joker if available and score a point. If second player doesn't have a requested card, they can play whatever they like. If a trump card is in play but was not requested by the first player and if second player doesn't have a requested card, but they have a trump card, they must play it and score a point.
* If second player doesn't have a suit which player who began the round has played, he/she can play whatever they like but the first player will score the point. But if trump card is in play and second player doesn't have a requested suit in their hand, but they have a trump card in their hand and/or on the board, they can play it and score a point.

## Technical design document
* Function user_names() for user's nickname inputs.
* Function total_cards_generator() to read .json file for cards and their values.
* GameSetup class for choosing a card distributor, trump card chooser and a player's choice for a trump card.
* three_card_distribution(), field_card_distribution() and remaining_card_distribution functions for distributing cards by a card distributor player.
* CardToPlay class for user's input for cards they play, using methods: any_card_to_play(), no_requested_card() and joker_action_request_card(). This class also handles removing played cards from either players hands or the board, adds joker to playable card pool if a player has joker. Additionally available_card_to_play_with_visuals() method prints cards with visuals instead of outputting a string.
* Function player_turn() returns an available card to play from a player for later utilization and comparison. This function will ask first player to play choose a card to play, if it did not receive previous_player_card when calling this function. Otherwise, it will return a second players card (an answer card to the first players card), which has all the needed restrictions, based by the rules, applied to it.
* deck_visualization.py file, applies visual effects to every single card. While users see only cards with visuals, the code handles everything with card codes, such as CA (as generated in the total_cards.json) for Ace of Clubs.
* main() function in main.py sums every function and class to create a full game.