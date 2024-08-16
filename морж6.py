s = '_abcdefgh'
coord_1 = input()
coord_2 = input()
letter = coord_1[0]
letter_2 = coord_2[0]
column1 = s.find(letter)
column2 = s.find(letter_2)
row1 = int(coord_1[1])
row2 = int(coord_2[1])
if (row1 + column1) % 2 == (row2 + column2) % 2:
    print("YES")
else:
    print("NO")


#Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том, являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.



#Программа должна выводить YES, когда клетки одного цвета, NO - разного. Гарантируется, что значение колонок это латинские буквы abcdefgh, а строки это символы цифр от 1-8



#Sample Input 1:

#a1
#b2
#Sample Output 1:

#YES











