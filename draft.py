import sys
import random


board = [[' ' for _ in range(3)] for _ in range(3)]
player_choice = 'X'
computer_choice = 'O'
games_won = 0
games_lost = 0
games_tied = 0
games_played = 0

def display_board():
    print("   0   1   2")
    print("  --- --- ---")
    for i in range(3):
        print(i, "|", end="")
        for j in range(3):
            print(board[i][j], "|", end="")
        print("\n  --- --- ---")



def check_win(symbol):
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False


def check_tie():
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True


def computer_option():
    row, col = -1, -1
    while board[row][col] != ' ':
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    board[row][col] = computer_choice


def player_option():
    row, col = -1, -1
    while row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
        try:
            row, col = map(int, input("Please enter 0-2 for row, and then 0-2 for column. Each number needs to be SEPARATED by a space for {}: ".format(player_choice)).split())
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid choice. Please pick between 0-2 for both row and column.")
        except ValueError:
            print("Invalid choice. Please pick between 0-2 for both row and column.")
    board[row][col] = player_choice


def write_stats_to_file(name):
    with open("TicTacToe.txt", "a") as outfile:
        outfile.write("{} played {} total games, won {} games, lost {} games,  and tied {} games.\n".format(name, games_played, games_won, games_lost, games_tied))

def play_game(name):
    global board, games_played, games_won, games_lost, games_tied, player_choice, computer_choice
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]
        player_choice = input("Please select and enter either X or O: ").upper()
        while player_choice not in ['X', 'O']:
            print("Invalid choice. Please pick between X and O.")
            player_choice = input("Please select and enter either X or O: ").upper()
        computer_choice = 'O' if player_choice == 'X' else 'X'
        display_board()
        while True:
            player_option()
            display_board()
            if check_win(player_choice):
                print("Well Done! You WIN!")
                games_played += 1
                games_won += 1
                break
            elif check_tie():
                print("Boring...Unfortunately it's a tie.")
                games_played += 1
                games_tied += 1
                break
            computer_option()
            display_board()
            if check_win(computer_choice):
                print("Ohh no! You lose...")
                games_played += 1
                games_lost += 1
                break
        play_again = input("Would you like to play again? Please enter (Y/N): ")
        if play_again == 'N':
            break
    write_stats_to_file(name)
    print("{} played {} total games, won {}, lost {}, and tied {}.\n".format(name, games_played, games_won, games_lost, games_tied))

def display_menu():
    print("1. Play Game")
    print("2. Description of game")
    print("3. Exit Game")
        

def main():
    print("Welcome to my Tic Tac Toe Game!")
    name = input("To begin, please enter your name: ")
    print("Welcome {}, lets get started.\n".format(name))
    while True:
        display_menu()
        decision = input("Select one of the following options: ")
        if decision == '1':
            play_game(name)
        elif decision == '2':
            print("This program runs your typical Tic Tac Toe game. Its player vs the computer, and the player always chooses first between 'X' and 'O'. Play as many times as you want! After you exiting the game your results will appear in the terminal, as well as in the output file.")
        elif decision == '3':
            print("Hope you enjoyed the game. See you next time!")
            break
        else:
            print("Option not available. Please select from options 1-3 on the menu.")

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def test_suite():
    global board
    board = [['O', 'X', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    test(check_win('X'))
    board = [[' ', 'O', 'X'], ['O', 'X', 'O'], ['X', ' ', 'O']]
    test(check_win('X'))
    board = [['X', 'X', ''], ['O', 'O', 'O'], ['X', 'X', ' ']]
    test(check_win('O'))
    board = [['O', 'X', 'X'], ['O', 'O', 'X'], ['O', 'X', ' ']]
    test(check_win('O'))
    board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    test(not check_win('X'))
    board = [['O', 'X', 'O'], ['O', 'O', 'X'], ['X', 'O', 'X']]
    test(not check_win('O'))
    board = [['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
    test(check_tie())
    board = [['O', 'X', 'O'], ['O', 'X', ' '], [' ', 'X', 'O']]
    test(not check_tie())

if __name__ == "__main__":
    main()
    test_suite()
