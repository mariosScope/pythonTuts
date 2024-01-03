import random

##Computer provides a guessing game of a number it has obtained.

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number :
        guess = int(input(f'Guess a number between 1 and {x}'))
        
        if guess > random_number :
            print('Your guess is too high, try harder')
        elif guess < random_number :
            print('Your guess is too low, try again')
        
    print(f'Great job, you have guessed the number {random_number} correclty')

##Now computer tries to guess a number selected by user

def computer_guess(x) :
    low = 1
    high = x
    feedback = ''
    guess = 0
    if low == high :
        feedback = 'c'
        guess = x
    while feedback != 'c' :
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)').lower()
        if feedback == 'h' :
            high = guess - 1
        elif feedback == 'l' :
            low = guess + 1
        elif feedback != 'c' :
            print ('That is not a valid option')
    print(f'Yay, I guessed! your number is {guess}. I am great, conqueror of worlds and stuff')

print("Let's play a game")
gameSelection = input("select 1 to guess a number or 2 for me to guess")
if gameSelection == '1' :
    guess(10)
elif gameSelection != '2' :
    print("Bye")
else :
    computer_guess(int(input('Give me a ceiling the base is 1')))
