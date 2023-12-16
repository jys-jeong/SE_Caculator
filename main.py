import sys
import getpass
import unittest
from unittest.mock import patch
import io

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

def factorial(num):
    if num<0:
        return "[ERROR] Out Of Range"
    return num * factorial(num-1) if num > 1 else 1

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
    if result[0]=='-':
        tmp=result[1:]
    else :
        tmp=result
    if not (str.isdigit(tmp)):
        intFlag = False
    else:
        if result in messages:  # 이스터에그인지 확인
            easter_egg(result)

        else:
            if result[0]=='-':
                result = float(tmp)
                result = -result
            else :
                result = float(tmp)

            while True:
                operator = input()

                if operator == '!':
                    factoend = input()
                    if factoend == '=':
                        result = factorial(result)
                        print(result)
                        return 0
                    else:
                        isCorrect = False
                        break
                    
                if operator == '=':
                    break

                if operator not in ('+', '-', '*') or (temp and temp != operator):
                    isCorrect = False
                else:
                    temp = operator

                next_num = str(input())
                if next_num[0]=='-':
                    tmp=next_num[1:]
                else :
                    tmp=next_num
                    
                if not (str.isdigit(tmp)):
                    intFlag = False
                    if(tmp=='='):
                        break
                else:
                    if next_num[0]=='-':
                        next_num=float(tmp)
                        next_num=-next_num
                    else :
                        next_num=float(tmp)
                    if operator == '+':
                        result = add(result, next_num)
                    elif operator == '-':
                        result = sub(result, next_num)
                    elif operator == '*':
                        result = mul(result, next_num)
                if not isCorrect and next_num=='!':
                    print("[ERROR] Input Error")
                    break
            if isCorrect and intFlag:
                print(int(result))
            elif not isCorrect and next_num=='!':
                print()
            else:
                print("[SYSTEM] ERROR!")



class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-5, -7), -12)

    def test_mul(self):
        self.assertEqual(mul(3, 5), 15)
        self.assertEqual(mul(-1, 1), -1)
        self.assertEqual(mul(0, 0), 0)
        self.assertEqual(mul(-5, -7), 35)
    def test_factorial(self):

        self.assertEqual(factorial(0), 1)

        self.assertEqual(factorial(-5), "[ERROR] Out Of Range")

        self.assertEqual(factorial(1), 1)

        self.assertEqual(factorial(2), 2)

        self.assertEqual(factorial(3), 6)

        self.assertEqual(factorial(10), 3628800)
    def test_easter_egg(self):
        # messages 딕셔너리에 있는 각 숫자에 대해 올바른 메시지가 출력되는지 테스트
        for num, message in messages.items():
            with self.subTest(num=num, message=message):
                with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                    easter_egg(num)
                    self.assertEqual(mock_stdout.getvalue().strip(), f"[EVENT] \"{message}\"")

        # messages 딕셔너리에 없는 숫자에 대해 출력이 없는지 테스트
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            easter_egg("123")
            self.assertEqual(mock_stdout.getvalue().strip(), "")
            

if __name__ =='__main__':
    calculator()
    unittest.main()