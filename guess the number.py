import random
max_attempt=5
attempt=0

number = random.randint(1, 10)

while attempt<max_attempt:
    guess = int(input("Enter your guess (1-10): "))
    attempt+=1
    if guess==number:
         print("Congratulations! You guessed correctly.")
         print(f'you guessed in {attempt} attempts')

        
    elif guess > number:
        print("Too High!")
        

    else :
        print("Too Low!")
        print(f'attempt left :{attempt}')

else:
    print("game over!")
    print(f'The correct number was {guess}')

