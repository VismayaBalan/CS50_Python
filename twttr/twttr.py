message = input("Input: ")
print("Output: ",end="")
for j in message:
    if j.lower() not in ['a', 'e', 'i', 'o', 'u']:
        print(j,end="")
print()