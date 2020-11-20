import sys
from game_of_greed.game_logic import Banker, GameLogic

class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.logic = GameLogic()
        self.num_rounds = num_rounds
        self._roller = GameLogic.roll_dice
        self.round_num = 0

    def play(self, roller=None):
        """Entry point for playing (or declining) a game
        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self.round_num = 0

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")

        response = input("> ")

        if response == "y" or response == "yes":
            self.start_game()
        else:
            self.decline_game()

    def decline_game(self):
        print("OK. Maybe another time")

    def new_roll(self, remaining_die):
        print(f"Rolling {remaining_die} dice...")
        die_roll = self._roller(remaining_die)
        string_roll = [str(num) for num in die_roll]
        return (die_roll, string_roll)

    def check_validity(self, die_roll, string_roll):
        cheated = True
        while cheated:
            cheated = False
            print(f'*** {" ".join(string_roll)} ***')
            round_points = self.logic.calculate_score(die_roll)
            if round_points == 0:
                return 'Zilch'
            print("Enter dice to keep, or (q)uit:")
            kept_die = input("> ")
            saved_die = list(kept_die)
            if kept_die == "q":
                print(f"Thanks for playing. You earned {self.banker.total} points")
                sys.exit()

            good_input = True
            for value in saved_die:
                try:
                    int(value)
                except:
                    saved_die.remove(value)

            user_selection = tuple(int(char) for char in saved_die)
            no_cheats = self.logic.validate_keepers(die_roll, user_selection)
            if not no_cheats:
                cheated = True
                print('Cheater!!! Or possibly made a typo...')
        return user_selection

    def round_decisions(self, remaining_die):
        print(f"You have {self.banker.shelved} unbanked points and {remaining_die} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        round_choice = input("> ")
        if round_choice == "q":
            print(f"Thanks for playing. You earned {self.banker.total} points")
            sys.exit()
        elif round_choice == "b":
            round_points = self.banker.bank()
            remaining_die = 6
            print(f"You banked {round_points} points in round {self.round_num}")
        elif round_choice == "r":
            if remaining_die == 0:
                remaining_die = 6
            self.full_roll(remaining_die)

    def full_roll(self, remaining_die):
        
        (die_roll, string_roll) = self.new_roll(remaining_die)
        user_selection = self.check_validity(die_roll, string_roll)

        if user_selection == 'Zilch':
            self.banker.clear_shelf()
            print('****************************************\n**        Zilch!!! Round over         **\n****************************************')
            print(f"You banked 0 points in round {self.round_num}")
        else:
            remaining_die -= len(user_selection)
            self.banker.shelf(self.logic.calculate_score(user_selection))
            self.round_decisions(remaining_die)

    def start_game(self):
        remaining_die = 6 
        
        while self.round_num < self.num_rounds:
            self.round_num += 1
            print(f"Starting round {self.round_num}")
            self.full_roll(remaining_die)
            print(f"Total score is {self.banker.total} points")

        print(f"Thanks for playing. You earned {self.banker.total} points")
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.play()