def main():
    time = input("What time is it? ")
    ft = convert(time)
    #print(ft)

    if 7 <= ft <= 8:
        print("Breakfast Time")
    elif 12 <= ft <= 13:
        print("Lunch Time")
    elif 18<= ft <= 19:
        print("Dinner Time")



def convert(tm):
    hours, mins = tm.split(":")
    hours = float(hours)
    mins = float(mins)
    mins = round(mins/60,2)

    ft_time = hours+mins

    return ft_time

if __name__ == "__main__":
    main()
