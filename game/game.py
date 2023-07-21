import random

while True:
    try:
        n = int(input('Level: '))
    except ValueError:
        continue
    else:
        if n > 0:
            break


ans = random.randint(1,n)
while True:
    try:
        guess = int(input('Guess: '))
    except ValueError:
        continue
    else:
        if guess > ans:
            print('Too Large!')
        elif guess < ans:
            print('Too Small!')
        else:
            print('Just right!')
            break














