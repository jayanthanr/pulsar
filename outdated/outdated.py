def main():
    mnth = [ "January",
              "February",
              "March",
              "April",
              "May",
              "June",
              "July",
              "August",
              "September",
              "October",
              "November",
              "December"]
   #print(ip_date)
    while True:
        ip_date = input("Date: ")
        ip_date = ip_date.strip()
        try:
            if "/" in ip_date:
                dm, dd, dy = ip_date.split(sep="/")
                #print(dm,dd,dy)
                if int(dm) < 1 or int(dm) > 12 or int(dd) > 31:
                    pass
                else:
                    dm = int(dm)
                    dd = int(dd)
                    print(dy+"-"+f"{dm:02}"+"-"+f"{dd:02}")
                    break
            elif "," in ip_date:
                cmmd, dy = ip_date.split(sep=",")
                dm, dd = cmmd.split(sep=" ")
                #print(dm,dd,dy)
                if dm not in mnth or int(dd) > 31:
                    pass
                else:
                    dm = mnth.index(dm)+1
                    dm = int(dm)
                    dd = int(dd)
                    print(dy+"-"+f"{dm:02}"+"-"+f"{dd:02}")
                    break
            else:
                pass
        except ValueError:
            pass


main()
