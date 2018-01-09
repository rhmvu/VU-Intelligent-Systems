from unittest import TestCase

from api import Deck, State
import random


class TestState(TestCase):


	#Use seed to deterministically generate a state for which
	#we know what should happen. Uses seed=50
	#Can possibly remove the asserts for get_card_states, perspectives might be enough.
	def test_trump_jack_exchange_deterministic(self):
		state = State.generate(50)
		self.assertEqual(state.get_deck().get_card_states(), ['P1H', 'P1H', 'S', 'S', 'P2H', 'P2H', 'S', 'P2H', 'P1H', 'P2H', 'S', 'P2H', 'S', 'S', 'P1H', 'S', 'P1H', 'S', 'S', 'S'])
		self.assertEqual(state.get_perspective(1), ['P1H', 'P1H', 'U', 'U', 'U', 'U', 'U', 'U', 'P1H', 'U', 'S', 'U', 'U', 'U', 'P1H', 'U', 'P1H', 'U', 'U', 'U'])
		self.assertEqual(state.get_perspective(2), ['U', 'U', 'U', 'U', 'P2H', 'P2H', 'U', 'P2H', 'U', 'P2H', 'S', 'P2H', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'])
		
		#Test trump jack exchange
		#Maybe needs to change if order of moves is altered
		self.assertEqual(state.whose_turn(), 1)
		self.assertEqual(state.get_points(1), 0)
		self.assertEqual(state.get_points(2), 0)
		self.assertEqual(state.get_pending_points(1), 0)
		self.assertEqual(state.get_pending_points(2), 0)

		state = state.next(state.moves().pop())
		self.assertEqual(state.whose_turn(), 1)
		self.assertEqual(state.get_deck().get_card_states(), ['P1H', 'P1H', 'S', 'S', 'P2H', 'P2H', 'S', 'P2H', 'P1H', 'P2H', 'P1H', 'P2H', 'S', 'S', 'S', 'S', 'P1H', 'S', 'S', 'S'])
		self.assertEqual(state.get_perspective(1), ['P1H', 'P1H', 'U', 'U', 'U', 'U', 'U', 'U', 'P1H', 'U', 'P1H', 'U', 'U', 'U', 'S', 'U', 'P1H', 'U', 'U', 'U'])
		self.assertEqual(state.get_perspective(2), ['U', 'U', 'U', 'U', 'P2H', 'P2H', 'U', 'P2H', 'U', 'P2H', 'P1H', 'P2H', 'U', 'U', 'S', 'U', 'U', 'U', 'U', 'U'])
		
		self.assertEqual(state.get_points(1), 0)
		self.assertEqual(state.get_points(2), 0)
		self.assertEqual(state.get_pending_points(1), 0)
		self.assertEqual(state.get_pending_points(2), 0)

	# Still in progress
	def test_marriage_deterministic(self):
		state = State.generate(38)
		self.assertEqual(state.get_deck().get_card_states(), ['S', 'P2H', 'P1H', 'S', 'P1H', 'P1H', 'S', 'S', 'P2H', 'S', 'S', 'P2H', 'P2H', 'P2H', 'S', 'S', 'S', 'S', 'P1H', 'P1H'])
		self.assertEqual(state.get_perspective(1), ['U', 'U', 'P1H', 'U', 'P1H', 'P1H', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'S', 'U', 'U', 'U', 'P1H', 'P1H'])
		self.assertEqual(state.get_perspective(2), ['U', 'P2H', 'U', 'U', 'U', 'U', 'U', 'U', 'P2H', 'U', 'U', 'P2H', 'P2H', 'P2H', 'S', 'U', 'U', 'U', 'U', 'U'])

	def test_next(self):
		# TODO: add sth?
		pass

	def test_finished(self):
		# TODO: add sth?
		pass

	def test_possible_move(self):
		#TODO implement after possible_move
		pass

	def test_next(self):
		# TODO implement after next
		pass

	def test_clone(self):
		deck = Deck.generate(0)
		state = State(deck,True)
		clone = state.clone()

		self.assertEqual(state.finished(), clone.finished())

		self.assertEqual(state.revoked(), clone.revoked())

		self.assertEqual(state.winner(), clone.winner())

		current_deck = state.get_deck()
		clone_deck = clone.get_deck()
		self.assertEqual(current_deck.get_card_states(), clone_deck.get_card_states())


		pass

	def test_game10(self):
		state = State.generate(0)

		for i in range(10):
			if not state.finished():
				moves = state.moves()
				state = state.next(moves[0])

	def test_game15(self):
		state = State.generate(0)

		for i in range(15):
			if not state.finished():
				# print state
				moves = state.moves()
				state = state.next(moves[0])

	def test_game_full(self):
		wins = 0
		for i in range(100000):
			state = State.generate()
			while not state.finished():
				moves = state.moves()
				# print state.get_deck().get_card_states()
				# print "p1 score: {}".format(state.get_points(1))
				# print "p2 score: {}".format(state.get_points(2))
				# print moves
				state = state.next(moves[0])

			winner, points = state.winner()
			if winner == 1:
				wins +=1
		print wins

	def test_seed_same(self):
		for i in range(1,1000):
			id = i
			s = State.generate(id)
			s1 = State.generate(id)
			if s.get_deck().get_card_states() != s1.get_deck().get_card_states() or s.whose_turn() != s.whose_turn():
				raise RuntimeError("The decks are not shuffled in the same way.")
				print s.get_deck().get_card_states()
				print s1.get_deck().get_card_states()

	def test_seed_different(self):
		s = State.generate()
		s1 = State.generate()
		if s.get_deck().get_card_states() == s1.get_deck().get_card_states():
			raise RuntimeError("The decks are shuffled in the same way.")
			print s.get_deck().get_card_states()
			print s1.get_deck().get_card_states()

	def test_exchange_visible(self):
		s = State.generate(11)
		moves = s.moves()
		print s.get_deck().get_card_states()
		print moves
		print s.get_deck().get_trump_suit()

	def test_exchange_move(self):
		s = State.generate(11)
		moves = s.moves()
		s1 = s.next(moves[5])

		if s.moves() == s1.moves():
			raise RuntimeError("The available moves should have changed.")
		if s.whose_turn() is not s1.whose_turn():
			raise RuntimeError("The turns shifted. This should not be the case.")
		if len(s.moves()) <= len(s1.moves()):
			raise RuntimeError("The number of available moves should have decreased.")
			#For finding states where a player can exchange (as long as mariage isn't enabled)
		# for i in range(1,100):
		# 	s = State.generate(i)
		# 	moves = s.moves()
		# 	if len(moves) > 5:
		# 		print s.get_deck().get_card_states()
		# 		print moves
		# 		print s.get_deck().get_trump_suit()
		# 		print i

	def test_mariage_visible(self):
		# for i in range(1,200):
		# 	s = State.generate(i)
		# 	moves = s.moves()
		# 	# if
		# 	print moves

		s = State.generate(2)
		moves = s.moves()
		# if
		print moves
