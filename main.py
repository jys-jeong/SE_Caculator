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

#유닛테스팅 클래스
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
            
calculator()
