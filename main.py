import sys


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def easter_egg(a):
    messages = {
        "1212": "I am 정종욱 교수님",
        "429": "I am 김소운",
        "803": "I am 황예찬",
        "1005": "I am 최아영",
        "903": "I am 정은주",
        "117": "I am 오주형",
        "725": "I am 정예성"
    }

    if a in messages:
        print(messages[a])
        # sys.exit()


def calculator():
    isCorrect = True  # '+', '-', '*' 이외의 연산자가 들어올 경우 False 처리
    intFlag = True # 정수 아닌 수가 들어오면 False
    temp = ""  # 한 가지 연산만 들어왔는지 판단하는 temp 변수
    res = str(input())
    if not (str.isdigit(res)):
        intFlag = False
    res = float(res)    
        
    while True:
        operator = input()

        # '=' 입력이 들어오면 계산 종료
        if (operator == '='):
            break

        # '+', '-', '*' 이외의 연산자가 들어올 경우 False 처리 + 이전 연산자와 다른 경우 False 처리
        if operator not in ('+', '-', '*') or (temp and temp != operator):
            isCorrect = False
        else:
            temp = operator

        # 가독성을 위해 num2 변수명 --> next_num으로 수정
        next_num = str(input())
        if not (str.isdigit(next_num)):
            intFlag = False
        next_num = float(next_num)

        if (operator == '+'):
            res = add(res, next_num)
        elif (operator == '-'):
            res = sub(res, next_num)
        elif (operator == '*'):
            res = mul(res, next_num)

    if isCorrect and intFlag:
            print(int(res))
            easter_egg(str(res))
    else:
        print("ERROR!!!")


calculator()
