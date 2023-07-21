import inflect

names=[]
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        p = inflect.engine()
        print("Adieu, adieu, to", p.join(names))
        break



