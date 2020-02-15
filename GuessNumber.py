import random
import sys
num = random.randint(1,100)
print('The number is between 1 and 100,Can you Guess it?? \n\n you have 5 attempts.')
for i in range(1,6):
    print("\nEnter the number")
    Guess = int(input())
    if Guess == num :
     print('\nyeaah you guessed it right!!')
     sys.exit()
    if Guess < num:
     print('\n Guessed number is smaller')
    elif Guess > num  :
     print('\n Guessed number is bigger')
print('\n Sorry, you have crossed the limits.\n\n THE NUMBER WAS  '+str(num))
sys.exit()
