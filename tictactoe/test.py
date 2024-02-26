from tictactoe import (
    X,
    O,
    EMPTY,
    player,
    initial_state,
    actions,
    result,
    winner,
    terminal,
)


x_board = [[X, EMPTY, O], [EMPTY, O, EMPTY], [X, EMPTY, EMPTY]]

o_board = [[EMPTY, EMPTY, EMPTY], [EMPTY, X, EMPTY], [EMPTY, EMPTY, EMPTY]]

winner_board = [[EMPTY, EMPTY, EMPTY], [X, X, X], [X, EMPTY, O]]

full_board = [[O, X, X], [X, O, O], [O, O, X]]


def print_board(board, name):
    print("=== ", name, " ===")
    for row in board:
        print(row)
    print("===============")


print("TEST: player()")

player_result_empty_state = player(initial_state())
player_result_x_state = player(x_board)
player_result_o_state = player(o_board)

# print("empty should be x: ", player_result_empty_state)
# print("x, should be x: ", player_result_x_state)
# print("o, should be o: ", player_result_o_state)

# print("TEST: actions()")

# print_board(o_board, "initial")
# print(actions(o_board))

# for action in actions(o_board):
#     print_board(result(o_board, action), action)

# print("TEST: result()")

# print_board(o_board, "initial")
# print_board(result(o_board, (2, 1)), "result")

print("TEST: winner()")

print(winner(winner_board))

# print("TEST: terminal()")

# print(terminal(full_board))
