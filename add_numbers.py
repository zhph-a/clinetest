# -*- coding: utf-8 -*-
"""
A simple script that prompts the user to enter two numbers and prints their sum.
"""

def main():
    try:
        a = float(input("请输入第一个数字: "))
        b = float(input("请输入第二个数字: "))
    except ValueError:
        print("请输入有效的数字")
        return
    print("结果:", a + b)

if __name__ == "__main__":
    main()
