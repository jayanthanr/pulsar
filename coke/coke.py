def main():
    amt_due = 50
    curr_amt_due = amt_due
    ttl_ip = 0
    print("Amount Due:",amt_due)
    # Insert cycle start
    while True:
        ip_amt = int(input("Insert Coin: "))
        if ip_amt == 25 or ip_amt == 10 or ip_amt == 5:
            ttl_ip = ttl_ip+ip_amt
            curr_amt_due = curr_amt_due-ip_amt
            if curr_amt_due > 0:
                print("Amount Due:",curr_amt_due)
            if ttl_ip >= 50:
                print("Change Owed:",(ttl_ip-amt_due))
                break
            else:
                pass
        else:
            print("Amount Due:",curr_amt_due)
            pass

main()
