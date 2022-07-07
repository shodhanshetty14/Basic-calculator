import calculator_functions as cal


while True:
    a = input("Enter the value of 'a': ")
    try:
        a = int(a)
    except:
        a = str(a)
        if a.lower() == 'stop':
            print('Program terminated')
            quit()
        
        break
    op = input("Enter a valid operator: ")
    if op.lower() == 'stop' or a.lower() == 'stop':
        print('Program terminated')
        quit()
    b = input("Enter the value of 'b': ")
    try:
        b = int(b)
    except:
        print("Enter a valid datatype")
        break
    if op == '+':
        answer = cal.add(a, b)
        print(f"The answer is{answer}")
    elif op.lower() == 'stop' or a.lower() == 'stop':
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
