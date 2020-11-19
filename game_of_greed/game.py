import sys
from game_of_greed.game_logic import Banker, GameLogic


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.num_rounds = num_rounds

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

    def new_roll(self, session, game_round, remaining_die):
        print(f"Rolling {remaining_die} dice...")
        die_roll = session.roll_dice(remaining_die)
        string_roll = [str(int) for int in die_roll]
        return (die_roll, string_roll)

    def check_validity(self, bank, die_roll, string_roll):
        cheated = True
        while cheated:
            cheated = False
            print(f'*** {" ".join(string_roll)} ***')
            print("Enter dice to keep, or (q)uit:")
            kept_die = input("> ")
            if kept_die == "q":
                print(f"Thanks for playing. You earned {bank.total} points")
                sys.exit()

            good_input = True
            for value in kept_die:
                try:
                    int(value)
                except:
                    good_input = False
            if good_input == False:
                cheated = True
                continue

            user_selection = tuple(int(char) for char in kept_die)
            for value in user_selection:
                if value not in die_roll:
                    cheated = True
            if cheated:
                print('Cheater!!! Or possibly made a typo...')
        return user_selection

    def round_decisions(self, session, bank, game_round, unbanked_points, remaining_die):
        print(f"You have {unbanked_points} unbanked points and {remaining_die} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        round_choice = input("> ")
        if round_choice == "q":
            print(f"Thanks for playing. You earned {bank.total} points")
            sys.exit()
        elif round_choice == "b":
            round_points = bank.bank()
            remaining_die = 6
            print(f"You banked {round_points} points in round {game_round}")
        elif round_choice == "r":
            bank.bank()
            if remaining_die == 0:
                remaining_die = 6
            self.full_roll(session, bank, game_round, remaining_die)

    def full_roll(self, session, bank, game_round, remaining_die):
        
        (die_roll, string_roll) = self.new_roll(session, game_round, remaining_die)
        user_selection = self.check_validity(bank, die_roll, string_roll)

        remaining_die -= len(user_selection)
        round_points = session.calculate_score(die_roll)
        bank.shelf(session.calculate_score(user_selection))
        unbanked_points = session.calculate_score(set(die_roll)- set(user_selection))

        if round_points == 0:
            print('****************************************\n**        Zilch!!! Round over         **\n****************************************')
            print(f"You banked {round_points} points in round {game_round}")
        else:
            self.round_decisions(session, bank, game_round, unbanked_points, remaining_die)

    def start_game(self):
        session = GameLogic()
        bank = Banker()
        game_round = 0
        remaining_die = 6 
        
        while bank.total < 10000:
            game_round += 1
            print(f"Starting round {game_round}")
            self.full_roll(session, bank, game_round, remaining_die)
            print(f"Total score is {bank.total} points")

if __name__ == "__main__":
    game = Game()
    game.play()