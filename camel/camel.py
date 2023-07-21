camel = input("camelCase: ")

print("snake_case: ",end="")
for i in camel:
    if (i.isupper()):
        print("_",end="")
    print(i.lower(),end="")
print()

