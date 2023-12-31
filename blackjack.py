import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}



#blackjack game!!
def main():
    game_on = True
    while True:
        print("Welcome to my Blackjack game!")

    #create and shuffle the deck
        game_deck = Deck()
        game_deck.shuffle()

    # deal two cards to each player
        dealer = Hand()
        player = Hand()
        dealer.add_card(game_deck.deal())
        dealer.add_card(game_deck.deal())

        player.add_card(game_deck.deal())
        player.add_card(game_deck.deal())

    #set up the player chips
        player_chips = Chips()

    #prompt the player for their bet
        #player_bet_amount = take_bet()

    #show cards(with one dealer card hidden)
        print("\nInitial cards dealt! \n")
        show_some(player, dealer)
        playing = True
        while playing:
            #ask if player wants to hit or stand
            hit_or_stand(game_deck,player)

            #show cards, keeping one dealer card hidden
            show_some(player, dealer)

            #if player has exceeded 21, run player bust and break out of loop
            if player.value > 21:
                player_busts(player, dealer, player_chips)
                playing = False
                break
            elif player.value == 21 and dealer_wins(player, dealer, player_chips):
                playing = False
                break

        #if player hasnt busted, play dealers hand until dealer reaches 17
            while dealer.value < 17:
                dealer.add_card(game_deck.deal())
                show_some(player, dealer)
            break

            #run differnet winning scenarios
        dealer_wins(player, dealer, player_chips)
        dealer_busts(player, dealer, player_chips)
        player_wins(player, dealer, player_chips)
        push(player, dealer, player_chips)

            #show all cards
        print(f"\nCards at end of game: ")
        show_all(player, dealer)

            #player total chips
        print(f"\nPlayer total chips at end of game: {player_chips.total}")

        play_again = input("\nPlay again? \n")
        if play_again.lower() in ["no", "n"]:
            game_on = False
            print("\nEnd of game")
            exit()
        elif play_again.lower() in ["yes", "y"]:
            game_on = True


#class to make cards
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

#deck of 52 cards
class Deck():
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.deck.append(created_card)

    def __str__(self):
        for item in self.deck:
            print(item)
        return f"Number of cards in the deck: {len(self.deck)}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

#hand class holds card objects dealt from deck
class Hand():
    def __init__(self):
        self.cards=[] #starts with an empty list
        self.value = 0 #start with zero
        self.aces = 0 #to keep track of
        # aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces+=1
#ace can be either 11 or 1 based on player game needs
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -=10
            self.aces -=1        
            

#class to track betting chips
class Chips():
    def __init__(self):
        self.total = 100 #default
        #self.bet = 0
        while True:
            self.bet_amount = take_bet()
            if self.bet_amount <= self.total:
                break
            else:
                print("You dont have enough chips!")
                

    def win_bet(self):
        
        self.total = self.total + (self.bet_amount*2)
        print(f"Amount won: {self.bet_amount*2} chips.")


    def lose_bet(self):
        
        self.total=self.total - self.bet_amount
        print(f"Amount lost: {self.bet_amount} chips.")


#asking user for bet amount
def take_bet():
    while True:
        bet_amount = input("Place your bet chip amount, numbers only: ")
        try:
            bet_amount = int(bet_amount)
            print(f"You have bet {bet_amount} chips.")
            return bet_amount
        except:
            print("That as not a number.")

#taking hits and check if ace present in hit
def hit(deck,hand):
    dealt_card = deck.deal()
    hand.add_card(dealt_card)
    hand.adjust_for_ace()

   
def hit_or_stand(deck,hand):
    global playing

    to_hit = input("Player: Hit or Stand? ")
    if to_hit.lower() == "hit":
        hit(deck,hand)
    elif to_hit.lower() == "stand":
        print("Player stands, Dealer's turn to play")
        playing = False
    else:
        print("invalid entry.")

#show cards played
def show_some(player, dealer):
    print(f"Dealer cards: \nHIDDEN FIRST CARD,")
    for card in dealer.cards[1:]:
        print(f"{card}, ")
    print(f"Total dealer score: {dealer.value}\n")

    print(f"Player cards: ")
    for card in player.cards:
        print(f"{card}, ")
    print(f"Total player score: {player.value}\n")


def show_all(player,dealer):
    print(f"\nDealer cards: ")
    for card in dealer.cards:
        print(f"{card}, ")
    print(f"Total dealer score: {dealer.value}\n")

    print(f"Player cards: ")
    for card in player.cards:
        print(f"{card}, ")
    print(f"Total player score: {player.value}\n")

#check game outcomes
def player_busts(players_hand, dealers_hand, chips):
    if players_hand.value > 21 and dealers_hand.value < 21:
        print("Player bust! :-(")
        chips.lose_bet()

def player_wins(players_hand,dealers_hand, chips):
    if players_hand.value <=21 and dealers_hand.value < 21 and players_hand.value > dealers_hand.value:
        print("Player wins!")
        chips.win_bet()

def dealer_busts(players_hand,dealers_hand,chips):
    if dealers_hand.value > 21 and players_hand.value < 21:
        print("Dealer bust!")
        chips.win_bet()

def dealer_wins(players_hand,dealers_hand,chips):
    if players_hand.value <21 and dealers_hand.value <= 21 and dealers_hand.value > players_hand.value:
        print("Dealer wins!")
        chips.lose_bet()

def push(players_hand,dealers_hand,chips):
    if players_hand.value <= 21 and dealers_hand.value <= 21 and (dealers_hand.value == players_hand.value):
        print("Truce!")
        chips.lose_bet()




if __name__ == "__main__":
    main()