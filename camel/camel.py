
def main():
    istr = input("Enter a variable name in camel case: ")
    ostr = ""

    for i in istr:
        if i.isupper():
            ostr = ostr+"_"+i.lower()
        else:
            ostr = ostr+i

    print("camelCase: ",istr)
    print("snake_case: ",ostr)

main()

