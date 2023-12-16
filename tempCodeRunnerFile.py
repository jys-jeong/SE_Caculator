class TestFunctions(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(3, 5), 8)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(0, 0), 0)
#         self.assertEqual(add(-5, -7), -12)

#     def test_mul(self):
#         self.assertEqual(mul(3, 5), 15)
#         self.assertEqual(mul(-1, 1), -1)
#         self.assertEqual(mul(0, 0), 0)
#         self.assertEqual(mul(-5, -7), 35)
#     def test_factorial(self):

#         self.assertEqual(factorial(0), 1)

#         with self.assertRaises(ValueError) as context:
#             factorial(-5)
#         self.assertEqual(str(context.exception), "[ERROR] Out Of Range")

#         with self.assertRaises(ValueError) as context:
#             factorial(2, 3)
#         self.assertEqual(str(context.exception), "[ERROR] Input Error")

#         self.assertEqual(factorial(1), 1)

#         self.assertEqual(factorial(2), 2)

#         self.assertEqual(factorial(3), 6)

#         self.assertEqual(factorial(10), 3628800)
#     def test_easter_egg(self):
#         # messages 딕셔너리에 있는 각 숫자에 대해 올바른 메시지가 출력되는지 테스트
#         for num, message in messages.items():
#             with self.subTest(num=num, message=message):
#                 with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
#                     easter_egg(num)
#                     self.assertEqual(mock_stdout.getvalue().strip(), f"[EVENT] \"{message}\"")

#         # messages 딕셔너리에 없는 숫자에 대해 출력이 없는지 테스트
#         with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
#             easter_egg("123")
#             self.assertEqual(mock_stdout.getvalue().strip(), "")