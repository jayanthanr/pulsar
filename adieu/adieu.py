import inflect

inf_eng = inflect.engine()

def main():
    lnam = []
    i = 0
    while True:
        try:
            ip = input("Name:")
            lnam.append(ip)
        except EOFError:
            print("", end="\n")
            break

    final_op = inf_eng.join(lnam)
    print("Adieu, adieu, to",final_op)

if __name__ == "__main__":
    main()



