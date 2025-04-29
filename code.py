import random

class Game:
    def __init__(self):
        self.choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.rules = { 
            "Rock": ["Scissors", "Lizard"], 
            "Paper": ["Rock", "Spock"], 
            "Scissors": ["Paper", "Lizard"], 
            "Lizard": ["Spock", "Paper"],
            "Spock": ["Scissors", "Rock"]
        }

    def start_game(self):
        player_name = input("Enter your name: ")
        player = Player(player_name)
        computer = Computer()
        
        while True: 
            player_choice = player.choose_option()
            computer_choice = computer.choose_option()

            self.determine_winner(player, computer, player_choice, computer_choice)
            self.display_result(player, computer)

            if not self.play_again():
                print("Thanks for playing!")
                break

    def determine_winner(self, player, computer, player_choice, computer_choice):
        print(f"{player.name} chose {player_choice}")
        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif computer_choice in self.rules[player_choice]:
            print(f"{player.name} wins this round!")
            player.update_score()
        else:
            print("Computer wins this round!")
            computer.update_score()

    def display_result(self, player, computer):
        print(f"{player.name}'s Score: {player.score} | Computer's Score: {computer.score}")

    def play_again(self):
        again = input('Do you want to play again? (yes/no): ')
        return again.lower() == 'yes'

class Player: 
    def __init__(self, name):
        self.name = name 
        self.score = 0 
    
    def choose_option(self):
        choice = input(f"{self.name}, choose Rock, Paper, Scissors, Lizard, or Spock: ")
        while choice not in ["Rock", "Paper", "Scissors", "Lizard", "Spock"]:
            print("Invalid choice. Try again.")
            choice = input(f"{self.name}, choose Rock, Paper, Scissors, Lizard, or Spock: ")
        return choice
    
    def update_score(self):
        self.score += 1 

class Computer:
    def __init__(self):
        self.score = 0 
    
    def choose_option(self):
        return random.choice(["Rock", "Paper", "Scissors", "Lizard", "Spock"])
    
    def update_score(self):
        self.score += 1 


if __name__ == "__main__":
    game = Game()
    game.start_game()
