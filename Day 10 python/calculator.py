#calculator 

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":divide
}

def calculator():
    num1= float(input("Entre The First Number : "))
    for symbol in operation:
        print(symbol)
    should_countinue= True

    while should_countinue:
        operation_symbol=input("Pick an operation : ")
        num2= float(input("Entre The Next Number : "))
        calculation_function = operation[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer }")

        if input(f"type 'y' to Countinue calculating with {answer}, or tpye 'n' to start a new calculation :")=="y":
            num1 = answer
        else:
            should_countinue = False
            calculator()
calculator()