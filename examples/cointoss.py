import random

def tosstoss():
    global toss,guess
    guess = ''
    toss = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    tosser = random.randint(0, 1) # 0 is tails, 1 is heads
    if tosser == 1:
        toss = 'heads'
    elif tosser == 0:
        toss = 'tails'
tosstoss()
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess Again!')
    tosstoss()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')