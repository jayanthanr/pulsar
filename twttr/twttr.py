def main():
    ip_str = input("Input: ")

    for i in ["a","A","e","E","i","I","o","O","u","U"]:
        ip_str = ip_str.replace(i,"")

    print("Output: "+ip_str)

main()
