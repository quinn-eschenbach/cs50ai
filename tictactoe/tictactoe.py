"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0

    for row in board:
        for field in row:
            if field != EMPTY:
                count += 1

    if count % 2 == 1:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i = row
    j = field
    """
    actions = set()

    for row_index, row in enumerate(board):
        for field_index, field in enumerate(row):
            if field == EMPTY:
                actions.add((row_index, field_index))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action[0] < 0 or action[0] > 3 or action[1] < 0 or action[1] > 3:
        raise Exception

    if action is None:
        raise TypeError

    new_board = copy.deepcopy(board)

    if new_board[action[0]][action[1]] is not EMPTY:
        raise Exception

    new_board[action[0]][action[1]] = player(new_board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check horizontaly
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check verticaly
    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # check diagonal to top right
    if board[2][0] == board[1][1] == board[0][2]:
        return board[2][0]

    # check diagonal to bottom right
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    not_empty = True
    for row in board:
        for field in row:
            if field == EMPTY:
                not_empty = False

    return not_empty


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    next_player = player(board)
    next_action = None

    v = -math.inf if next_player is X else math.inf

    for action in actions(board):
        if next_player is X:
            min_v = min_value(result(board, action))
            if min_v > v:
                next_action = action
                v = min_v
        else:
            max_v = max_value(result(board, action))
            if max_v < v:
                next_action = action
                v = max_v

    return next_action


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v