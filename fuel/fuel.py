def main():
    xnum = 0
    ynum = 0
    while xnum==0:
        try:
            fract = input("Fraction: ")
            xnum, ynum = fract.split("/")
            xnum = int(xnum)
            ynum = int(ynum)

            if xnum > ynum:
                xnum = 0
                pass
            elif ynum == 0:
                xnum = 0
                pass
            else:
                #pct = ("{:.0%}".format(x/y))
                pct = int((xnum/ynum)*100)
                if pct <= 1:
                    print("E")
                elif pct >= 99:
                    print("F")
                else:
                    #print(pct)
                    print("{:.0%}".format(xnum/ynum))
                break
        except ValueError:
            xnum = 0
            pass

main()

