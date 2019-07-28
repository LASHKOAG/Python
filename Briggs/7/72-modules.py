import time

#asctime() возвращает текущие дату и время в виде строки
#Sun Jul 28 21:02:10 2019
print(time.asctime())

#*******************************************************
import sys
#взаимодействие с интерпретатором

#напечатаем строчку введенную пользователем
print(sys.stdin.readline())
#*******************************************************

def age_joke(age):
    if age >=10 and age <=13:
        print("Step 1")
    elif age < 10:
        print("Step 0")
    else :
        print("Step 3")

your_age = int(sys.stdin.readline())
age_joke(your_age)
#********************************************************

