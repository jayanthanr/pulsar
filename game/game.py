import random
import sys

def main():

    ip = 0
    gnum = 0

    while True:
        try:
            ip = int(input("Level:"))
            if ip < 0:
                pass
            elif ip > 0:
                break
        except ValueError:
            pass

    while True:
        try:
            gnum = int(input("Guess:"))
            if gnum < 0:
                pass
            elif gnum > 0:
                break
        except ValueError:
            pass

    rand = random.randint(1,ip)
    if gnum == rand:
        sys.exit("Just Right!")
    elif gnum < rand:
        print("Too small!")
    elif gnum > rand:
        print("Too large!")

main()
