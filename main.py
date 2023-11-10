import sys
import getpass

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def easter_egg(number):
    messages = {
        "1212": "I am 정종욱 교수님",
        "429": "I am 김소운",
        "803": "I am 황예찬",
        "1005": "I am 최아영",
        "903": "I am 정은주",
        "117": "I am 오주형",
        "725": "I am 정예성"
    }

    if number in messages:
        print(messages[number])

def calculator():
    isCorrect = True  # '+', '-', '*' 이외의 연산자가 들어올 경우 False 처리
    intFlag = True # 정수 아닌 수가 들어오면 False
    temp = ""  # 한 가지 연산만 들어왔는지 판단하는 temp 변수
    result = str(input())
    if not (str.isdigit(result)):
        intFlag = False
    result = float(result)    
        
    while True:
        operator = input()

        if operator == '=':
            break

        if operator not in ('+', '-', '*') or (temp and temp != operator):
            isCorrect = False
        else:
            temp = operator

        next_num = str(input())
        if not (str.isdigit(next_num)):
            intFlag = False
        next_num = float(next_num)

        if operator == '+':
            result = add(result, next_num)
        elif operator == '-':
            result = sub(result, next_num)
        elif operator == '*':
            result = mul(result, next_num)

    if isCorrect and intFlag:
        print(int(result))
        easter_egg(str(int(result)))
    else:
        print("ERROR!")

calculator()
