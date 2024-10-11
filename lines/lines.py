import sys

def main():
    #Check the number of arguements passed
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')

    countline = 0

    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".py"):
            try:
                with open(sys.argv[1], "r") as file:
                    for line in file:
                        row = line.lstrip()
                        if row.startswith("#"):
                            pass
                        elif len(row.strip())==0:
                            pass
                        else:
                            countline = countline+1
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a Python file')

        print(countline)

if __name__ == '__main__':
    main()

