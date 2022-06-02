from random import randint


"""
LEVEL 1 : Create a die to roll for the game randomly

"""
class Dye(object):
    """
   The class is focused on our Dye as an object: to generate random numbers ranging from 1 to 6 for players,
                                                 then zero number to generate a faul play
    """

    def __init__(self):  # Our attributes are intended to be instance attributes
        pass

    def roll(self):    # Declaring! A method that let our Dye roll
        return randint(0, 6)

        # Generating random numbers rolled on our Dye

class Block(object):  # A Class for our Block on our Board game
    """
    Data Attributes:name
    """
    def __init__(self, name):  # It's neccessary to declare our object
        self.name = name
    # Declaring our objects for seperation concerns
    def trigger_event(self):
        print("Basic Block Action Caused")

"""
 LEVEL 2: Declaring our locations
 
 """
class Property(Block):
    """
    Data Attributes:name, price, base_rent, is_utility, is_rr, owner
   The class attribute definitions run once
    """
    def __init__(self, name, price, base_rent, is_utility=False,
                 is_rr=False):
        self.name = name
        self.price = price
        self.base_rent = base_rent
        self.owner=None

        if (is_utility):
            self.is_utility = True
        if (is_rr):
            self.is_rr = True

    def trigger_event(self):
        if self.owner is None:
            print("You have now arrived on an unclaimed property.")

            while True:
                print("\n", "Menu of Unclaimed Property")
                Game.display_menu(Game.unowned_property_menu)
                selection = input("Enter a number to select an option.: ")

                """
                If statement let user to buy unclaimed property with enough credit or to choose to not buy
                """
                if selection == '1':
                    # Allows a player to purchase  Property that is unclaimed
                    if Game.current_player.balance >= self.price:
                        Game.current_player.owned_properties.append(self)
                        Game.current_player.balance -= self.price
                        print("Congratulations!", Game.current_player.name,
                              "has successfully purchsed", self.name,
                              "for the price of R", self.price)
                        Game.current_player.display_balance()
                    else:
                        print("Your balance of", Game.current_player.balance,
                              "seems to be insufficient to purchase", self.name, "at the price of R",
                              self.price)

                    break
                elif selection == '2':
                    # Do Not Buy Property
                    print("You chose not to buy {}.".format(self.name))
                    break
                else:
                   print("Error option selected!")

    def view_property(self):
        print("Property Purchsed: " + self.name)


class Player(object):
    """
    Class Attributes: player_list/max_num_players

    Data Attributes: name/ current_tile_index/ current_tile/ is_in_jail/ properties_owned / amount_of_money

    """
    player_list = [] #starting position of players
    MAX_NUM_PLAYERS = 3



    def __init__(self, name):
        if len(Player.player_list) == Player.MAX_NUM_PLAYERS:
            print("Error: Cannot have more than", Player.MAX_NUM_PLAYERS, "players!")  # Displays limits notice for a number players
        else: # Declaring variables we gonna need
            self.name = name
            self.roll = [0]
            self.current_block_index = 0
            self.current_block = None # sets current tile to "Begin the Game"
            self.is_in_jail = False
            self.num_rounds_in_jail = 0
            self.owned_properties = []
            self.balance = 15000  # initial amount for each player as they begin the game

            Player.player_list.append(self)
            print(self.name, "has been succesfully added with an Initial SASSA amount of R15 000.00!") # Display the output

    def roll_and_move(self):  #  a method from one class that is dependent on a data property from another
        roll_1 = Game.DYE.roll()
        roll_2 = Game.DYE.roll()
        total_roll = roll_1 + roll_2

        print(self.name, "You just rolled a", total_roll) # Display the output
        """print("You just rolled a", roll_2) # Display the output"""

        if (roll_1) == 0:
            print(" ")
            print(" ----- ")
            print("|DIE    |")
            print("|FELL ON|")
            print("|GROUND |")
            print(" -----   ")
            print(" ")
        elif (roll_1) == 1:
            print(" ")
            print(" ----- ")
            print("|      |")
            print("|  O   |")
            print("|      |")
            print(" ----- ")
            print(" ")
        elif roll_1 == 2:
            print(" ")
            print(" ----- ")
            print("|    O |")
            print("|      |")
            print("| O    |")
            print(" ----- ")
            print(" ")
        elif roll_1 == 3:
            print(" ----- ")
            print("| O    |")
            print("|  O   |")
            print("|    O |")
            print(" ----- ")
            print(" ")
        elif roll_1 == 4:
            print(" ----- ")
            print("| O  O |")
            print("|      |")
            print("| O  O |")
            print(" ----- ")
            print(" ")
        elif roll_1 == 5:
            print(" ----- ")
            print("| O  O |")
            print("|  O   |")
            print("| O  O |")
            print(" ----- ")
            print(" ")
        elif roll_1 == 6:
            print(" ----- ")
            print("| O  O |")
            print("| O  O |")
            print("| O  O |")
            print(" ----- ")
            print(" ")

        if roll_2 == 0:
            print(" ")
            print(" ----- ")
            print("|DIE    |")
            print("|FELL ON|")
            print("|GROUND |")
            print(" -----   ")
            print(" ")
        elif roll_2 == 1:
            print(" ")
            print(" ----- ")
            print("|      |")
            print("|  O   |")
            print("|      |")
            print(" ----- ")
            print(" ")
        elif roll_2== 2:
            print(" ")
            print(" ----- ")
            print("|    O |")
            print("|      |")
            print("| O    |")
            print(" ----- ")
            print(" ")
        elif roll_2 == 3:
            print(" ----- ")
            print("| O    |")
            print("|  O   |")
            print("|    O |")
            print(" ----- ")
            print(" ")
        elif roll_2 == 4:
            print(" ----- ")
            print("| O  O |")
            print("|      |")
            print("| O  O |")
            print(" ----- ")
            print(" ")
        elif roll_2 == 5:
            print(" ----- ")
            print("| O  O |")
            print("|  O   |")
            print("| O  O |")
            print(" ----- ")
            print(" ")
        elif roll_2 == 6:
            print(" ----- ")
            print("| O  O |")
            print("| O  O |")
            print("| O  O |")
            print(" ----- ")
            print(" ")

        # move player to new block
        if total_roll + self.current_block_index >= len(Game.BOARD):
            final_index = (self.current_block_index + total_roll) - len(Game.BOARD)
            self.current_block_index = final_index
            self.current_block = Game.BOARD[self.current_block_index]
            self.balance += 2000  # Allocating a grant when a player Pass a Begin tile.
            print("You passed Proceed!")  # Display the output
        else:
            self.current_block_index = self.current_block_index + total_roll
            self.current_block = Game.BOARD[self.current_block_index]

        print("Your current Location is now in ",self.current_block.name)    # Display the output

        # trigger_event
        self.current_block.trigger_event()

    def display_owned_properties(self):
        print("{}'s Properties: ".format(self.name))
        for property in self.owned_properties:
            print(property.name)

    def display_balance(self):
        print("{}'s current balance is R{}".format(self.name, self.balance)) # Passing current balance with referencing

    def get_out_of_jail(self):
        pass  # Code to be rectified


    """
    Function that let other players join and play the game."""
    def add_player(self):
        if len(Player.player_list) == Player.max_num_players:
            print("Error, cannot have more than",Player.max_num_players, "players")
            return
        else:
            print("You are adding a player")
            name = input('Please type the name of the player: ')
            Player.player_list.append(Player(name))
            for player in Player.player_list: # other players are added to the list.
                print(player.name, "successfully added!") 


"""It's time to create instances for our locations in our game board"""
class Game(object):
    """ Only initialize once so that it may execute once."""
    current_player = None
    next_player = None
    turn_counter = 0
    DYE = Dye()
    BOARD = None
    setup_menu = None
    player_menu = None
    unowned_property_menu = None
    exit_game = 0

    """LEVEL 2: Assigning Locations on function for the board game"""
    def __init__(self):
        """
        Creating our board Game, listing all locations required
        """
        Game.BOARD = [         # using '[' & ']' make it easier for on seperate lines
            Block("Begin"),
            Property("Sandton hotel", 4000, 2),
            Block("Community Chest-Jozi"),
            Property("Braamfontein B&B",2500, 8),
            Block("Brixton-Jail"),
            Property("NorthCliff Heights", 1000, 50),
            Block("Chance"),
            Property("Kingsway-Accomodation", 4000, 6),
            Property("Memory Space", 500, 6),
            Block("Campus-Square Free Parking"),
            Property("Melville house", 2500, 8),
            Block("Chance"),
            Block("Go straight to Brixton-jail"),
            Property("Cache de Cookie", 3000, 10),
            Property("Auckland Park Flats", 6000, 0),
            Block("Community Chest-Soweto")]

        Game.setup_menu = {}
        Game.setup_menu['1'] = "Add Player."
        Game.setup_menu['2'] = "Start Game."
        Game.setup_menu['3'] = "Exit The Game"

        Game.player_menu = {}
        Game.player_menu['1'] = "Roll Dice."
        Game.player_menu['2'] = "Display Owned Properties."
        Game.player_menu['3'] = "Exit The Game"       # LEVEL 3: Allows a player to exit the game

        Game.unowned_property_menu = {}
        Game.unowned_property_menu['1'] = "Buy Property"
        Game.unowned_property_menu['2'] = "Do Not Buy Property"


        print("Welcome to Amazing Monopoly 2022!")
        while True:      # Allow player to have options to play the game until the game ends
            print("\n")
            Game.display_menu(Game.setup_menu)
            selection = input("Select an option by typing a number: ")
            if selection == '1':
                player_name = input("Please enter player Name: ")
                Player(player_name)
            elif selection == '2':
                if len(Player.player_list) == 0:
                    print("Error: Cannot start game without players")
                else:
                    break
            elif selection == '3':
                # Let player exit the game
                print("**************** - Game Cancelled!!! - ***************")
                exit(0)
            else:
               print("Unknown option selected!")


        Game.current_player= Player.player_list[0]
        self.main() # Starts The  Main Game for players to play.

        # end of  Loop.


    def display_menu(menu: dict):
        for option in menu:
            print("{}. {}".format(option, menu[option]))


    def start_player_turn(self):
        if Game.current_player.is_in_jail:
            did_his_time = Game.current_player.num_turns_in_jail == 3
            if did_his_time:
                Game.current_player.get_out_of_jail()
            else:
                print(self.Game.current_player.is_in_jail)

        elif True==False:  # if player ran out of money
            pass
        else:
            while True:
                print("\n", "Player Menu:")
                Game.display_menu(Game.player_menu)
                selection = input("Select an option by typing a number: ")
                if selection == '1':
                    # Let player move on the board game by rolling a dye
                    Game.current_player.roll_and_move()
                elif selection == '2':
                    # Let player to view their purchased property
                    print("Property owned: Scroll up to view your Owned Property")



                elif selection == '3':
                   # Let player exit the game
                    print("**************** -Game Over- ***************")
                    exit(0)
                else:
                   print("Unknown option selected")



    def main(self): # function checks if players landed in jail tiles
        while True:
            if Game.current_player.is_in_jail:
                self.end_player_turn()
            elif True == False:
                pass # all other players bankrupt, end game
            else:
                self.start_player_turn()



if __name__ == "__main__":
    Game()   # Turning back to the set up of  menu so the player can keep playing the game
