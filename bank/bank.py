def main():
    ip = input("Greeting: ")
    ip = ip.strip().lower()
    op = chk_greeting(ip)
    print(op)

def chk_greeting(in_str):
    if in_str.startswith("hello"):
        return "$0"
    elif in_str.startswith("h"):
        return "$20"
    else:
        return "$100"

main()


