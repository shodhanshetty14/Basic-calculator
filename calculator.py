import calculator_functions as cal


while True:
    a = input("Enter the value of 'a': ")
    try:
        a = int(a)
    except:
        print("Enter a valid datatype")
        break
    op = input("Enter a valid operator: ")
    b = input("Enter the value of 'b': ")
    try:
        b = int(b)
    except:
        print("Enter a valid datatype")
        break
    if op == '+':
        answer = cal.add(a, b)
        print(f"The answer is{answer}")
    elif op.lower() == 'stop':
        print('Program terminated')
        quit()
    elif op == '-':
        answer = cal.sub(a, b)
        print(f"The answer is{answer}")
    elif op == '*':
        answer = cal.multiply(a, b)
        print(f"The answer is{answer}")
    elif op == '/':
        answer = cal.div(a, b)
        print(f"The answer is{answer}")
    else:
        print("It's an INVALID Operator")
