import emoji

def main():
    ip = input("Input: ")
    print("Output:",emoji.emojize(ip, language='alias'))

if __name__ == "__main__":
    main()
