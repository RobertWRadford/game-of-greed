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



    def start_game(self):
        session = GameLogic()
        game_round = 0
        point_total = 0
        remaing_die = 6 
        
        while point_total< 10000:
            game_round += 1
            print(f"Starting round {game_round}")
            print(f"Rolling {remaing_die} dice...")
<<<<<<< HEAD
            die_roll = session.roll_dice(remaing_die)
            string_roll = [str(int) for int in die_roll]
            print(f'*** {" ".join(string_roll)} ***')
=======
            die_roll = session.roll_dice(remaing_die)  
            string_roll = [str(int) for int in die_roll]
            print(f'*** {string_roll} ***')
>>>>>>> 9bea4cb31d828044f2d6a524a710154456615efa
            print("Enter dice to keep, or (q)uit:")
            kept_die = input("> ")
            if kept_die == "q":
                print(f"Thanks for playing. You earned {point_total} points")
                break
            user_selection = tuple(int(char)for char in kept_die)
            remaing_die -= len(user_selection)
            shelf_points = session.calculate_score(user_selection)
            round_points = session.calculate_score(die_roll)
            unbanked_points = session.calculate_score(set(die_roll)- set(user_selection))
            if round_points == 0:
                print('****************************************\n**        Zilch!!! Round over         **\n****************************************')
                print(f"You banked {round_points} points in round {game_round}")
            else:
                print(f"You have {unbanked_points} unbanked points and {remaing_die} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                round_choice = input("> ")
                if round_choice == "q":
                    print(f"Thanks for playing. You earned {point_total} points")
                    break
                elif round_choice == "b":
                    point_total += round_points
                    remaing_die = 6
                    print(f"You banked {round_points} points in round {game_round}")
                elif round_choice == "r":
                    point_total += shelf_points
            print(f"Total score is {point_total} points")
<<<<<<< HEAD
                    
=======

                    










        


>>>>>>> 9bea4cb31d828044f2d6a524a710154456615efa
if __name__ == "__main__":
    game = Game()
    game.play()