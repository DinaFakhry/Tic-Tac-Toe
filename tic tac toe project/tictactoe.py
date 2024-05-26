import os
def clear_screan():
    os.system("cls" if os.name == "nt" else "clear")

class Player:

    def __init__(self) :
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter your name (letter only):")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name, Please use letters only.")

    def choose_symbol(self):
        while True: 
            symbol = input(f"{self.name},choose your symbol (a single letter)")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please choose a single letter.")     

class Menu:
    
    def display_main_menu(self):
        print("Welcome to my X-O game!")  
        print("1. Start Game")
        print("2. Quit Game")  
        return self.validate_choice()
        
       
        

    def display_endgame_menu(self):  
        menu_text = """
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter your choice (1 or 2): """
        print(menu_text)
        return self.validate_choice()

    def validate_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice (1 or 2):"))
                if choice == 1 or choice == 2:
                    return choice
            except ValueError:
                print("Please enter (1 or 2):")

class Board:
    def __init__(self):
        self.board = [str(i)for i in range(1,10)]

    def display_board(self):
        for i in range(0, 9, 3):
            print("|".join(self.board[i:i+3]))
            if i<6:
                print("-"*5)
    
    def update_board(self,choice,symbol):
        if self.is_valid_move(choice):
            self.board[choice-1] = symbol
            return True
        return False
    
    def is_valid_move(self,choice):
        return self.board[choice - 1].isdigit()
    
    def reset_board(self):
        self.board = [str(i)for i in range(1,10)]

class Game:
    def __init__(self):
        self.players = [Player(),Player()]
        self.board = Board()
        self.menu = Menu()  
        self.currunt_player_index = 0

    def start_game(self):
        choice = str(self.menu.display_main_menu()) 
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()
    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player{number},enter your details:")
            player.choose_name()
            player.choose_symbol()
            clear_screan()
    
    def play_game(self):
        while True: 
            self.play_turn()
            winner_symbol = self.check_win()
            if winner_symbol or self.check_draw():
                self.board.display_board()
                if winner_symbol:
                    winner = next(player for player in self.players if player.symbol == winner_symbol)
                    print(f"{winner.name} is the winner!")  
                else:
                    print("It's a draw!")
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    

    def restart_game(self):
        self.board.reset_board()
        self.currunt_player_index = 0
        self.play_game()

    def check_win(self):
        win_combinations = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal from top-left to bottom-right
            [2, 4, 6]   # Diagonal from top-right to bottom-left
        ]

        for combo in win_combinations:
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return self.board.board[combo[0]]  # Return the symbol of the winner

        return None
        

    def check_draw(self):
         
         return all(not cell.isdigit() for cell in self.board.board)

    def play_turn(self):
        player = self.players[self.currunt_player_index]
        self.board.display_board()
        print(f"{player.name}'s turn({player.symbol})")
        while True:
            try:
                cell_choice = input("Choose a cell (1-9):")
                cell_choice = int(cell_choice)
                if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):

                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        self.switch_player()
    def switch_player(self):
        self.currunt_player_index = 1 - self.currunt_player_index

    def quit_game(self):
        print("Thank you for Playing!")
     
game = Game()
game.start_game()
        