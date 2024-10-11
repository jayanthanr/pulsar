import random
import sys

def main():
    level = get_level()

    score = 0

    for i in range(10):
        a = generate_integer(level)
        b = generate_integer(level)

        for j in range(3):
            ans = input(f"{a} + {b} =")
            if int(ans) == int(a + b):
                score += 1
                break
            else:
                print("EEE")
                if j == 2:
                    print(a+b)
            j += 1

        i += 1

    print(f"Score: {score}")
    sys.exit(0)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                level = input()
            else:
                break
        except ValueError:
            level = input()
    return level


def generate_integer(level):
    if level == 1:
        randnum = random.randint(0, 9)
    elif level == 2:
        randnum = random.randint(10, 99)
    elif level == 3:
        randnum = random.randint(100, 999)
    else:
        raise ValueError

    return randnum


if __name__ == "__main__":
    main()
