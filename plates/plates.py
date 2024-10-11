def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    #first condition - All plates must start withat least two letters
    if s[0:2].isdigit():
        return False

    #second condition - Max 6 characters and Min 2 characters
    if len(s) < 2 or len(s) > 6:
        return False

    #third condition - Alphanumeric check
    i=0
    while i<len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i = i+1

    #third condition - no character after number
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False

    #fourth condition - No Period, space and punctuation marks
    for i in s:
        if i in ["."," ","!","?"]:
            return False

    #
    #Final
    #
    return True

main()
