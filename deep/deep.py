def main():
    in_str = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    in_str = in_str.strip()
    ouput = check_42(in_str)
    print(ouput)

def check_42(ip):
    if ip == "42":
        return "Yes"
    elif ip.lower() == "forty-two":
        return "Yes"
    elif ip.lower() == "forty two":
        return "Yes"
    else:
        return "No"

main()





