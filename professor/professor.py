import random
import sys

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)

        for j in range(3):
            ans = input(f"{a} + {b} = ")
            if int(ans) == int(a + b):
                score += 1
                break
            else:
                print("EEE")
                if j == 2:
                    print(a + b)

    print(f"Score: {score}")
    sys.exit(0)

def get_level():
    while True:
        try:
            level = int(input("Enter level (1, 2, or 3): "))
            if level < 1 or level > 3:
                print("Invalid level. Please enter 1, 2, or 3.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")
    return level

def generate_integer(level):
    if level == 1:
        y = random.randint(0, 9)
    elif level == 2:
        y = random.randint(10, 99)
    elif level == 3:
        y = random.randint(100, 999)
    else:
        raise ValueError("Invalid level")
    return y

if __name__ == "__main__":
    main()
