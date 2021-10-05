import random
secret_number = random.randint(0,2)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count +=1
    if guess == secret_number:
           print('You won!')
    else:
          print('haar gaye!')
         
