import sys
import getpass

messages = {
    "1212": "I am 정종욱 교수님",
    "429": "I am 김소운",
    "803": "I am 황예찬",
    "1005": "I am 최아영",
    "903": "I am 정은주",
    "117": "I am 오주형",
    "725": "I am 정예성",
    "1015": "전북대 개교기념일입니다."
}

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

# 기존 이스터에그는 "="를 쳐야 나오는데
# 이스터에그 숫자만 치면 나오도록 변경

def easter_egg(number):
    if number in messages:
        print("[EVENT] \"" + messages[number] + "\"")

def calculator():
    isCorrect = True  # '+', '-', '*' 이외의 연산자가 들어올 경우 False 처리
    intFlag = True  # 정수 아닌 수가 들어오면 False
    temp = ""  # 한 가지 연산만 들어왔는지 판단하는 temp 변수

    result = str(input())
    if not (str.isdigit(result)):
        intFlag = False

    else:
        if result in messages:  # 이스터에그인지 확인
            easter_egg(result)

        else:
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
            else:
                print("[SYSTEM] ERROR!")
#아래로 유닛 테스팅용 함수
def addTest():
    print("add함수 테스트 결과: ")
    tc = [(-10, 1), (10, -20), (0, 0)]
    ans = [-9, -10, 0]
    
    for i in range(3):
        if add(tc[i][0], tc[i][1]) != ans[i]:
            return False
    return True

def mulTest():
    print("mul함수 테스트 결과: ")
    tc = [(-10, 2), (5, -3), (0, 10)]
    ans = [-20, -15, 0]
    
    for i in range(3):
        if mul(tc[i][0], tc[i][1]) != ans[i]:
            return False
    return True

def easter_eggTest():
    test_cases = ["1212", "429", "803", "1005", "903", "117", "725", "1015", "1111"]
    expected_results = {
        "1212": "I am 정종욱 교수님",
        "429": "I am 김소운",
        "803": "I am 황예찬",
        "1005": "I am 최아영",
        "903": "I am 정은주",
        "117": "I am 오주형",
        "725": "I am 정예성",
        "1015": "전북대 개교기념일입니다."
    }

    for case in test_cases:
        print(f"Testing with input {case}:")
        easter_egg(case)
        expected_result = expected_results.get(case, "메시지가 안나와야합니다")
        print(f"Expected: {expected_result}")
        print("=" * 30)
#유닛 테스팅용 함수 끝
print(addTest())
print(mulTest())
print(easter_eggTest())

calculator()
