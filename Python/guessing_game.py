#Create a friendly Guess the Number game
#Asks you for your name and uses it in the game
#Tells you that you need to go higher or lower when you guess wrong
#Max of 5 guesses per game and then tells you that you lost
#Tells you that you won when you won
import random

user_name = raw_input("Hi there! Tell me your name: ")

print "Hello " +user_name+ "! Let's play a game! I'm thinking of a number between 1 and 10."
guesses = 5

computer_guess = random.randint(1,10)
#print computer_guess

while guesses > 0:
	user_guess = raw_input("What's your guess?: ")
	user_guess = int(user_guess)
	if user_guess > computer_guess:
		print "Nope! Lower!"
		guesses -= 1
		print "You have " + str(guesses) +  " guesses left" 
		if guesses == 0:
			print "Sorry, " + user_name +" you lost. The number was " + str(computer_guess)

	elif user_guess < computer_guess:
		print "Nope! Higher!"
		guesses -= 1
		print "You have " + str(guesses) +  " guesses left" 
		if guesses == 0:
			print "Sorry, " + user_name +" you lost. The number was " + str(computer_guess)

	elif user_guess == computer_guess:
		print "Yes! You win,"+  user_name+ "! Congrats!"
		guesses = 0

	
