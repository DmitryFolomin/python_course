a = float(input())
b = float(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/' and b != 0:
    print(a / b)
else:
    print('Неизвестно')

#Калькулятор своими руками
#Напишите программу, которая считывает с клавиатуры два вещественных числа, а затем строку. Если эта строка является обозначением одной из четырёх основных математических операций (+, -, * или /),
# то выведите результат применения этой операции к введенным ранее числам, в противном случае выведите «Неизвестно». Также «Неизвестно» следует вывести, если пользователь захочет поделить на ноль.

#Входные данные
#Два вещественных числа в каждой отдельной строчки. На третьей строке вводится символ операции

#Выходные данные
#Необходимо посчитать значение операции «+», «-», «*», «/». Если ввели символ, который не относится к данным операциям, необходимо вывести «Неизвестно». «Неизвестно» также выводится при попытке деления на ноль

#Sample Input 1:

#3.5
#2.5
#+
#Sample Output 1:

#6.0
#Sample Input 2:

#5
#2
#/
#Sample Output 2:

#2.5
#Sample Input 3:

#5
#0
#/
#S#ample Output 3:

#Неизвестно
#Sample Input 4:

#7
#8
#?
#Sample Output 4:

#Неизвестно




















