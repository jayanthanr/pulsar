def main():
    ip = input("Expression: ")
    x,y,z = ip.split(" ")
    #print(x,":",y,":",z)
    x = float(x)
    z = float(z)

    if y == "+":
        op = round(x+z,1)
    elif y == "-":
        op = round(x-z,1)
    elif y == "*":
        op = round(x*z,1)
    elif y == "/":
        op = round(x/z,1)

    print(op)

main()
