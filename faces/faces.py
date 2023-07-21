def main():
    n = input()
    n = convert(n)
    print(n)

def convert(a):
    a=a.replace(":)","🙂")
    a=a.replace(":(","🙁")
    return a

main()