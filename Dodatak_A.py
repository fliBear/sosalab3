import os
import getpass
import ast
import math


class OperationsManager:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def perform_division(self) -> float:
        """Divides a with b. If b is zero, returns NaN."""
        if self.b == 0:
            return math.nan
        return self.a / self.b


def login_success():
    a = float(input("A = "))
    b = float(input("B = "))
    ops_manager = OperationsManager(a, b)
    print(ops_manager.perform_division())

    expression = input("Enter a mathematical formula to calculate: ")
    print("Result: ", ast.literal_eval(expression))


def safeCheckPass(password):
    f = open("password.txt", "r")
    saferPassCheck = f.read()
    return password == saferPassCheck


if __name__ == "__main__":
    user = input("Username: ")
    password = getpass.getpass("Password: ")
    if user != "root" or not safeCheckPass(password):
        print("Wrong username or password!")
        exit(0)
    else:
        print("Login success!")
        login_success()
