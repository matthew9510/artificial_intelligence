from basicsearch_lib.boardtypes import TileBoard
print("HOW TO PLAY: ")
print("After entering the specified size of the N-puzzle, you will be shown possible actions.")
print("\n")
print("The possible actions are in the form, [row_shift, column_shift]")
print("[0, 1] -> Move the blank tile one column to the right")
print("[0, -1] -> Move the blank tile one column to the left")
print("[1, 0] -> Move the blank tile one row up")
print("[-1, 0] -> Move the blank tile one row down")
print("\n")
print("In order to make a move, simply enter the desired action by typing in a number designated to move, and then press enter")
print("OBJECTIVE: Get board to solved state")
print("\n")

n_puzzle_size = int(input("Please enter the size of the N-Puzzle you'd like to play: "))
game_board = TileBoard(n_puzzle_size)
dict = {}
print("OBJECTIVE, GOAL STATE:")
print(game_board.get_goal_state(n_puzzle_size))
print("\n" * 2)
print("Current state: ")
print(game_board)

while not game_board.solved():
    print("Possible actions: ")
    for k, v in enumerate(game_board.get_actions(), 1):
        print(k, v)
        dict[k] = v
    desired_move = int(input("Enter in your move: "))
    # Print(game_board.move(dict[desired_move]))  # Error in logic
    game_board = game_board.move(dict[desired_move])
    print(game_board)

print("Good job you win!")