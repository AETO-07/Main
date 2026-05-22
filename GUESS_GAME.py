import random

randomNumber = random.randint(1, 100)
attempts = 0
max_attempts = 5
print("You have 5 attempts to guess the number")
while attempts < max_attempts:
    try:
        guess = int(input("Enter a number (1 - 100): "))
        attempts += 1
        if guess == randomNumber:
            print(f"Correct!, You got it in {attempts} attempts.")
            break
        elif guess > randomNumber:
            print("Too High")
        else:
            print("Too low")
    except ValueError:
        print("Please enter a valid integer.")
    print(f"You have {max_attempts - attempts} attempts left")

if  guess != randomNumber and attempts == max_attempts:
            print(f"Game Over, {attempts} attempts used already. The number is {randomNumber}")
         