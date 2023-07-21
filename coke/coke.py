price = 50
print("Amount Due:",price)
while True:
    coin = int(input("Insert Coin: "))

    if coin not in [25,10,5]:
        print("Amount Due:",price)
    else:
        balance = price - coin
        price = balance
        if balance>0:
            print("Amount Due:",balance)
        elif balance <= 0:
            print("Change Owed:",abs(balance))
            break


