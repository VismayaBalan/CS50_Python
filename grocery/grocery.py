d = {}
while True:
    try:
        items= input().splitlines()


    except EOFError:
        for item in sorted(d):
            print(str(d[item])+' '+ item.upper())
        break
    else:
        try:
            for item in items:
                if item in d:
                    d[item] += 1
                else:
                    d[item] = 1
        except KeyError:
            items= input().splitlines()











