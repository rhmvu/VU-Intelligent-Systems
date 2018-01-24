import kb, sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
# J1 is true if the card with index 1 is a jack, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')
PJ0 = Boolean('pj0')
PJ1 = Boolean('pj1')
PJ2 = Boolean('pj2')
PJ3 = Boolean('pj3')
PJ4 = Boolean('pj4')
PJ5 = Boolean('pj5')
PJ6 = Boolean('pj6')
PJ7 = Boolean('pj7')
PJ8 = Boolean('pj8')
PJ9 = Boolean('pj9')
PJ10 = Boolean('pj10')
PJ11 = Boolean('pj11')
PJ12 = Boolean('pj12')
PJ13 = Boolean('pj13')
PJ14 = Boolean('pj14')
PJ15 = Boolean('pj15')
PJ16 = Boolean('pj16')
PJ17 = Boolean('pj17')
PJ18 = Boolean('pj18')
PJ19 = Boolean('pj19')



A0 = Boolean('a0')
A1 = Boolean('a1')
A2 = Boolean('a2')
A3 = Boolean('a3')
A4 = Boolean('a4')
A5 = Boolean('a5')
A6 = Boolean('a6')
A7 = Boolean('a7')
A8 = Boolean('a8')
A9 = Boolean('a9')
A10 = Boolean('a10')
A11 = Boolean('a11')
A12 = Boolean('a12')
A13 = Boolean('a13')
A14 = Boolean('a14')
A15 = Boolean('a15')
A16 = Boolean('a16')
A17 = Boolean('a17')
A18 = Boolean('a18')
A19 = Boolean('a19')
PA0 = Boolean('pa0')
PA1 = Boolean('pa1')
PA2 = Boolean('pa2')
PA3 = Boolean('pa3')
PA4 = Boolean('pa4')
PA5 = Boolean('pa5')
PA6 = Boolean('pa6')
PA7 = Boolean('pa7')
PA8 = Boolean('pa8')
PA9 = Boolean('pa9')
PA10 = Boolean('pa10')
PA11 = Boolean('pa11')
PA12 = Boolean('pa12')
PA13 = Boolean('pa13')
PA14 = Boolean('pa14')
PA15 = Boolean('pa15')
PA16 = Boolean('pa16')
PA17 = Boolean('pa17')
PA18 = Boolean('pa18')
PA19 = Boolean('pa19')

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
# This adds information which cards are Jacks
kb.add_clause(J4)
kb.add_clause(J9)
kb.add_clause(J14)
kb.add_clause(J19)
# Add here whatever is needed for your strategy.
kb.add_clause(A0)
kb.add_clause(A5)
kb.add_clause(A10)
kb.add_clause(A15)

# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
# PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
# In other words that the PJ strategy should play a card when it is a jack
"""
kb.add_clause(~J4, PJ4)
kb.add_clause(~J9, PJ9)
kb.add_clause(~J14, PJ14)
kb.add_clause(~J19, PJ19)
kb.add_clause(~PJ4, J4)
kb.add_clause(~PJ9, J9)
kb.add_clause(~PJ14, J14)
kb.add_clause(~PJ19, J19)
"""

# Add here other strategies

#PLAY ACE STRATEGY
kb.add_clause(~A0, PA0)
kb.add_clause(~A5, PA5)
kb.add_clause(~A10, PA10)
kb.add_clause(~A15, PA15)
kb.add_clause(~PA0, A0)
kb.add_clause(~PA5, A5)
kb.add_clause(~PA10, A10)
kb.add_clause(~PA15, A15)

kb.add_clause(~PA0)

#kb.add_clause(~PJ4)
# Print all models of the knowledge base
for model in kb.models():
    print model

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print kb.satisfiable()
