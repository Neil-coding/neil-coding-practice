from random import randrange

secret = randrange(0, 200)

attempts = 0
max_attempts = 10

while True:
    print('Remaining attempts: ' + str(max_attempts - attempts) + '/' + str(max_attempts))
    if attempts >= max_attempts:
        print("You've ran out of attempts")
        print('The number was ' + str(secret))
        break # END THE LOOP
    
    guess = int(input('What is your guess? '))
    attempts += 1
    if secret > guess:
        print('The number is higher than ' + str(guess))
        continue # SKIP TO NEXT LOOP IMMEDIATELY
    if guess > secret:
        print('The number is lower than ' + str(guess))
        continue # SKIP TO NEXT LOOP IMMEDIATELY
    if guess == secret:
        print('You guessed it!')
        break # END THE LOOP

print("game over")
