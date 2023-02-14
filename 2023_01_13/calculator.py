while True:
    a = float(int(input('n1:')))
    b = float(int(input('n2:')))
    if a==0 and b==0:
        break
    op = input('연산자:')
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a/b)