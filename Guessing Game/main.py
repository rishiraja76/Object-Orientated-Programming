#Importing package
import random

#Declarations
number = random.randint(1,101) #Random number to guess
ubound=number+10 #Upper bound of players guess
lbound=number-10 #Lower bound of players guess
flag = False #Check for game session
turn = 0 #Count the turns
temp = 0 #Placeholder for players guess
guess = 0 #Players input

#Game in duration
while flag == False:
    #Take in the players guess
    guess = int(input(print("Enter a number between 1 and 100")))
    #Check if its within 1 and 100
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue
    turn = turn + 1
    #Check if the guess is right
    if guess==number:
        print("CORRECT! You took {} guesses".format(turn))
    #On the first turn check the closeness within 10 digits of the guess
    elif turn==1:
       if guess<=ubound and guess>=lbound:
            print("WARM!")
       else:
            print("COLD!")
       temp=guess
    #On consecutive turns check if the guess is getting closer or further
    else:
        if abs(temp-number) > abs(guess-number):
            print("WARMER!")
        else:
            print("COLDER!")
        temp=guess
