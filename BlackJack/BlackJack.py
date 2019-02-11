
from random import shuffle
import random

card_values = {"2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "10": 10,
               "J": 10,
               "Q": 10,
               "K": 10,
               "A": 11,
               }

class Deck():
    def __init__(self):
        self.cards = []
        for _ in range(1, 4):
            self.cards.extend(card_values.keys())

        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player():
    def __init__(self):
        self.cards = []

    def print_cards(self):
        return ", ".join(self.cards)

    def score(self):
        score = sum([card_values[c] for c in self.cards])
        return score if score <= 21 else -1  # -1 means you busted

    def draw(self, deck, stop_limit):
        if (self.score() >= 21 or self.score() == -1):
            return False
        if(self.score() <= stop_limit):
            self.cards.append(deck.draw())
            return True


class HousePlayer(Player):
    def __init__(self, target_score):
        super().__init__()
        self.target_score = target_score
        
    def draw(self, deck):
        while self.score() < self.target_score and self.score() >= 0:
            self.cards.append(deck.draw())
            return True

class Patterns():

    def __init__(self, wins, loss):
        self.wins = wins
        self.loss= loss

    def run_pattern_one(self):
        # Run simulation with 17 as stop
        player = Player()
        deck = Deck()

        while player.draw(deck, 17):
            print("You have %s (=%d)." % (player.print_cards(), player.score()))

        house = HousePlayer(player.score())
        while house.draw(deck):
            print("House has %s (=%d)." % (house.print_cards(), house.score()))

        if (player.score() > house.score()):
            print("You won!")
            self.wins += 1
        else:
            print("You lost!")
            self.loss += 1

        print("\nWins with pattern one: ", self.wins)
        print("Losses with pattern one: ", self.loss)


    def run_pattern_two(self):
        # Run simulation with random number between 16 and 19 as stop
        stop_limit = random.randint(16, 19)
        player = Player()
        deck = Deck()

        while player.draw(deck, stop_limit):
            print("You have %s (=%d)." % (player.print_cards(), player.score()))

        house = HousePlayer(player.score())
        while house.draw(deck):
            print("House has %s (=%d)." % (house.print_cards(), house.score()))

        if (player.score() > house.score()):
            print("You won!")
            self.wins += 1
        else:
            print("You lost!")
            self.loss += 1

        print("\nWins with pattern two: ", self.wins)
        print("Losses with pattern two: ", self.loss)



if __name__ == "__main__":

    input("\nRun games 200 times with pattern one?")
    patterns = Patterns(0, 0);
    for x in range(0, 200):
        patterns.run_pattern_one()

    input("\nRun games 200 times with pattern two?")
    patterns = Patterns(0, 0);
    for x in range(0, 200):
        patterns.run_pattern_two()
