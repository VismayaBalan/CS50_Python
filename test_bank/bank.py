def main():
    s = input("Greeting: ")
    print(value(s))

def value(s):

    if "hello" in s.lower():
        return 0
    elif s[0].lower()=="h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()