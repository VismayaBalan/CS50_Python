n = input("Expression: ").split()
a = float(n[0])
b = float(n[2])
if n[1] == '+':
    print("%.1f" %(a+b))
elif n[1] == '-':
    print("%.1f" %(a-b))
elif n[1] == '*':
    print("%.1f" %(a*b))
elif n[1] == '/':
    print("%.1f" %(a/b))

