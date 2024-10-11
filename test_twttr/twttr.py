def main():
    ip_str = input("Input: ")
    print("Output: "+shorten(ip_str))


def shorten(word):
    for i in ["a","A","e","E","i","I","o","O","u","U"]:
        word = word.replace(i,"")

    return word


if __name__ == "__main__":
    main()
