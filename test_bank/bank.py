def main():
    ip = input("Greeting: ")
    #ip = ip.strip().lower()
    op = value(ip)
    #print(op)
    print(f"${op}")

def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
