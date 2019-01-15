from random import randint

"""Guess the Number Game """

computer_number = 45
player_number = eval(input('Guess a number: '))

if player_number == computer_number:
    message = 'Winner!'
else:
    message = 'Not a winner!'

print(message)
print(computer_number)
print(player_number)