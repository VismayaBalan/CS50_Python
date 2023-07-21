while True:
    try:
        a,b = input("Fraction: ").split('/')
        percentage = int(a) / int(b)*100
    except ValueError:
        a,b = input("Fraction: ").split('/')
    except ZeroDivisionError:
        a,b = input("Fraction: ").split('/')

    else:
        if (100 >= percentage >= 99 ):
            print("F")
            break
        elif (int(a) > int(b)):
          a,b = input("Fraction: ").split('/')
        elif (percentage <= 1):
            print('E')
            break
        else:
            print(str(round(percentage)) + "%")
            break

