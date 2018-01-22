#!/usr/bin/env python
"""


"""

from api import State, util
import random

class Bot:

    __max_depth = -1
    __randomize = True

    def __init__(self, randomize=True, depth=4):
        """
        :param randomize: Whether to select randomly from moves of equal value (or to select the first always)
        :param depth:
        """
        self.__randomize = randomize
        self.__max_depth = depth

    def get_move(self, state):
        # type: (State) -> tuple[int, int]

        val, move = self.value(state)

        return move

    def value(self, state, depth = 0):
        # type: (State, int) -> tuple[float, tuple[int, int]]
        """
        Return the value of this state and the associated move
        :param state:
        :param depth:
        :return: A tuple containing the value of this state, and the best move for the player currently to move
        """
        if state.finished():
            return (1.0, None) if state.winner() == 1 else (-1.0, None)

        if depth == self.__max_depth:
            return heuristic(state)

        moves = state.moves()

        if self.__randomize:
            random.shuffle(moves)

        best_value = float('-inf') if maximizing(state) else float('inf')
        best_move = None

        for move in moves:

            next_state = state.next(move)

            # IMPLEMENT: Add a recursive function call so that 'value' will contain the
            # minimax value of 'next_state'
            value = self.value(next_state,depth+1)[0]

            if maximizing(state):
                if value > best_value:
                    best_value = value
                    best_move = move
            else:
                if value < best_value:
                    best_value = value
                    best_move = move

        return best_value, best_move

def maximizing(state):
    # type: (State) -> bool
    """
    :param state:
    :return: True if we're the maximizing player (player 1), false otherwise (player 2).
    """
    return state.whose_turn() == 1

def heuristic(state):
    # type: (State) -> float
    """
    Estimate the value of this state: -1.0 is a certain win for player 2, 1.0 is a certain win for player 1

    :param state:
    :return: A heuristic evaluation for the given state (between -1.0 and 1.0)
    """
    return ratio_high_cards(state), None
    if amount_of_trumps(state) == 0:
        return 1 ,None
    else:
        return float(1/amount_of_trumps(state)), None
    return util.ratio_points(state, 1) * 2.0 - 1.0, None

def amount_of_trumps(state):
    amount = 0
    for card in state.hand():
        if util.get_suit(card) == state.get_trump_suit():
            amount+=1
    return amount

def amount_of_marraiges(state):
    for card in state.hand():
        if util.get_card_name(card) == "Q":
            pass

def ratio_high_cards(state):
    amount = 0
    for card in state.hand():
        rank = util.get_rank(card)
        suit = util.get_suit(card)
        if rank in ["K","10","A"] or suit == state.get_trump_suit():
            amount+=1;
    return amount/len(state.hand())