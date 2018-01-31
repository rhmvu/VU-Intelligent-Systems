#!/usr/bin/env python
"""
A basic adaptive bot. This is part of the third worksheet.

"""

from api import State, util, Deck
import random, os

from sklearn.externals import joblib

# Path of the model we will use. If you make a model
# with a different name, point this line to its path.
DEFAULT_MODEL = os.path.dirname(os.path.realpath(__file__)) + '/model.pkl'


class Bot:
    __randomize = True

    __model = None

    def __init__(self, randomize=True, model_file=DEFAULT_MODEL):

        print(model_file)
        self.__randomize = randomize

        # Load the model
        self.__model = joblib.load(model_file)

    def get_move(self, state):

        val, move = self.value(state)

        return move

    def value(self, state):
        """
        Return the value of this state and the associated move
        :param state:
        :return: val, move: the value of the state, and the best move.
        """

        best_value = float('-inf') if maximizing(state) else float('inf')
        best_move = None

        moves = state.moves()

        if self.__randomize:
            random.shuffle(moves)

        for move in moves:

            next_state = state.next(move)

            # IMPLEMENT: Add a function call so that 'value' will
            # contain the predicted value of 'next_state'
            # NOTE: This is different from the line in the minimax/alphabeta bot
            value = self.heuristic(next_state)

            if maximizing(state):
                if value > best_value:
                    best_value = value
                    best_move = move
            else:
                if value < best_value:
                    best_value = value
                    best_move = move

        return best_value, best_move

    def heuristic(self, state):

        # Convert the state to a feature vector
        feature_vector = [features(state)]

        # These are the classes: ('won', 'lost')
        classes = list(self.__model.classes_)

        # Ask the model for a prediction
        # This returns a probability for each class
        prob = self.__model.predict_proba(feature_vector)[0]

        # Weigh the win/loss outcomes (-1 and 1) by their probabilities
        res = -1.0 * prob[classes.index('lost')] + 1.0 * prob[classes.index('won')]

        return res


def maximizing(state):
    """
    Whether we're the maximizing player (1) or the minimizing player (2).
    :param state:
    :return:
    """
    return state.whose_turn() == 1


def features(state):
    # type: (State) -> tuple[float, ...]
    """
    Extract features from this state. Remember that every feature vector returned should have the same length.

    :param state: A state to be converted to a feature vector
    :return: A tuple of floats: a feature vector representing this state.
    """

    feature_set = []

    perspective = state.get_perspective()

    # Convert the card state array containing strings, to an array of integers.
    # The integers here just represent card state IDs. In a way they can be
    # thought of as arbitrary, as long as they are different from each other.
    perspective = [card if card != 'U' else (-1) for card in perspective]
    perspective = [card if card != 'S' else 0 for card in perspective]
    perspective = [card if card != 'P1H' else 1 for card in perspective]
    perspective = [card if card != 'P2H' else 2 for card in perspective]
    perspective = [card if card != 'P1W' else 3 for card in perspective]
    perspective = [card if card != 'P2W' else 4 for card in perspective]
    feature_set += perspective

    # Add player 1's points to feature set
    p1_points = state.get_points(1)
    feature_set.append(p1_points)

    # Add player 2's points to feature set
    p2_points = state.get_points(2)
    feature_set.append(p2_points)

    # Add player 1's pending points to feature set
    p1_pending_points = state.get_pending_points(1)
    feature_set.append(p1_pending_points)

    # Add player 2's pending points to feature set
    p2_pending_points = state.get_pending_points(2)
    feature_set.append(p2_pending_points)

    # Difference between points
    point_difference = abs(max(p1_points, p2_points) - min(p1_points, p2_points))
    feature_set.append(point_difference)

    # Difference between pending points
    pending_point_difference = abs(
        max(p1_pending_points, p2_pending_points) - min(p1_pending_points, p2_pending_points))
    feature_set.append(pending_point_difference)

    # Get trump suit
    trump_suit = state.get_trump_suit()

    # Convert trump suit to id and add to feature set
    # You don't need to add anything to this part
    suits = ["C", "D", "H", "S"]
    trump_suit_id = suits.index(trump_suit)
    feature_set.append(trump_suit_id)

    # Trump card ratio:
    cards = state.hand()
    trump_card_count = 0
    for card in cards:
        if Deck.get_suit(cards[0]) == state.get_trump_suit():
            trump_card_count += 1
    if trump_card_count != 0:
        trump_card_count = (trump_card_count / len(state.hand())) * 100
    feature_set.append(trump_card_count)

    # High ranking cards ratio:
    high_rank_count = 0
    for card in cards:
        if Deck.get_rank(cards[0]) == "A" or Deck.get_rank(cards[0]) == "10":
            high_rank_count += 1
    if high_rank_count != 0:
        high_rank_count = (high_rank_count / len(state.hand())) * 100
    feature_set.append(high_rank_count)

    # Add phase to feature set
    phase = state.get_phase()
    feature_set.append(phase)

    # Number of trump cards in phase 2:
    phase2_trump_cards = 0
    if phase == 2:
        phase2_trump_cards = trump_card_count ** 2
        feature_set.append(phase2_trump_cards)
    else:
        feature_set.append(phase2_trump_cards)

    # Add stock size to feature set
    stock_size = state.get_stock_size()
    feature_set.append(stock_size)

    # Add leader to feature set
    leader = state.leader()
    feature_set.append(leader)

    # Add whose turn it is to feature set
    whose_turn = state.whose_turn()
    feature_set.append(whose_turn)

    # Add opponent's played card to feature set
    opponents_played_card = state.get_opponents_played_card()

    # You don't need to add anything to this part
    opponents_played_card = opponents_played_card if opponents_played_card is not None else -1
    feature_set.append(opponents_played_card)

    # Do I have cards in same suit as oppponent?
    same_suit_cards = 0
    for card in cards:
        if Deck.get_suit(cards[0]) == Deck.get_suit(opponents_played_card):
            same_suit_cards += 1
    feature_set.append(same_suit_cards)

    # Get number of points in hand
    cards = state.hand()
    number_of_points = 0
    for card in cards:
        if cards[0] is not None:
            if Deck.get_rank(cards[0]) == "J":
                number_of_points += 1 ** 2
            elif Deck.get_rank(cards[0]) == "Q":
                number_of_points += 2 ** 2
            elif Deck.get_rank(cards[0]) == "K":
                number_of_points += 3 ** 2
            elif Deck.get_rank(cards[0]) == "10":
                number_of_points += 10 ** 2
            elif Deck.get_rank(cards[0]) == "A":
                number_of_points += 11 ** 2

    feature_set.append(number_of_points)
    return feature_set
