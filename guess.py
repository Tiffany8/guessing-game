# psuedocode:
# greet player
# get player name
# choose random number between 1 and 100
# while True:
#     get guess
#     if guess is incorrect:
#         give hint
#     else:
#         congratulate player
""" This is a computer guessing game.  The computer guesses a number from 1 to 100, asks the user to guess the number, 
and provides the user hints on whether too high or low. """

#first, greeting the user - the comma removes the invisible line break and prints the two statements on the same line
print "Howdy, partner!",
print "What's your name?"
user_name = raw_input("Please type your name: ")

#Tests to ensure that user_name is bound to the user's input
print user_name, "<-- The user name prints"
