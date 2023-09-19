import math
import os
def checkInt():
    while(True):
        firstNumber = input()
        if firstNumber.isdigit():
            return int(firstNumber)
        else:
            print("Вы ввели не число")
            continue
clear = lambda: os.system('cls')
lastresult= ("")
bool  (True)
while (True):
    clear()
    print ("Последний результат " + str(lastresult))
    print("Введите действие (end для завершения работы программы)")
    action = input()
    if action == "end":
        break
    print("Введите первое число")
    firstNumber = checkInt()
    print("Введите второе число")
    secondNumber = checkInt()
    match action:
        case "+":
            lastresult =(firstNumber + secondNumber)
        case "-":
            lastresult =(firstNumber - secondNumber)
        case "*":
            lastresult =(firstNumber * secondNumber)
        case "/":
            if secondNumber == 0:
                print("Делить на ноль нельзя")
            else:
                lastresult =(firstNumber / secondNumber)
        case "tan":
                lastresult =( math.tan (firstNumber))
        case "sin":
                lastresult =(math.sin(firstNumber))
        case "cos":
                lastresult =(math.cos(firstNumber))
        case "!":
            lastresult =(math.factorial(firstNumber))
        case "sqrt":
                lastresult =(math.sqrt(firstNumber))
        case "^":
                lastresult =(firstNumber ** secondNumber)
        case _:
                print("Неизвестная операция")
    print (lastresult)