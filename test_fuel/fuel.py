def main():
    num = input("Fraction: ")
    percentage = convert(num)
    print(gauge(percentage))




def convert(num):
    while True:
        try:
            a,b = num.split('/')
            a = int(a)
            b = int(b)
            percentage = a / b * 100
            if (a>b):
                a,b = input("Fraction: ").split('/')
        except ValueError:
            raise
        except ZeroDivisionError:
            raise
        else:
            return percentage


def gauge(percentage):
    while True:
        if (100 >= percentage >= 99 ):
            return 'F'


        elif (percentage <= 1):
            return 'E'
        else:
            return str(round(percentage)) + "%"



if __name__ == "__main__":
    main()