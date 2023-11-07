def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def calculate():
    res = int(input("Input number: "))

    while True:
        operator = input("연산자(+, -, *, = 중 하나를 입력하세요): ")

        if operator == '=':
            print("The result:", res)
            break

        num2 = int(input("Input number: "))

        if operator == '+':
            res = add(res, num2)
        elif operator == '-':
            res = sub(res, num2)
        elif operator == '*':
            res = mul(res, num2)

calculate()
