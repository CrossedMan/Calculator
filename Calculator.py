def calculator(numb_1, numb_2, op):
    if op == "+":
        result = numb_1 + numb_2
    elif op == "-":
        result = numb_1 - numb_2
    elif op == "*":
        result = numb_1 * numb_2
    print(f"{numb_1} {op} {numb_2} = {result}")


numb_1 = int(input("First number "))
op = input("Operator: ")
numb_2 = int(input("Other number: "))

calculator(numb_1, numb_2, op)
