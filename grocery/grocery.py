def main():
    #
    glist = {}
    while True:
        try:
            itm = input()
            if itm.upper() in glist:
                glist[itm.upper()] = glist[itm.upper()]+1
                pass
            else:
                glist[itm.upper()] = 1
                pass
        except EOFError:
            print("", end="\n")
            break

    for i in sorted(glist):
        print(glist[i],i)

main()
