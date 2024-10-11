def main():
    menu = {
        "Baja Taco":4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    #itm = input("Item: ")
    total = 0
    while True:
        try:
            itm = input("Item: ")
            if itm.title() in menu:
                total = total+menu[itm.title()]
                print("Total:",('${:,.2f}'.format(total)))
                pass
            else:
                pass
        except KeyError:
            pass
        except EOFError:
            print("", end="\n")
            break
    #print(total)

main()


