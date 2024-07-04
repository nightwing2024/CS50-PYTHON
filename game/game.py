import random

# Loop input
while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            print("Level must be greater than 0.")
            continue
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Random number
n = random.randint(1, level)

# Loop guess
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1 or guess > level:
            if guess < 1:
                print("Too small!")
            else:
                print("Too large!")
            continue
        elif guess < n:
            print("Too small!")
        elif guess > n:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue
