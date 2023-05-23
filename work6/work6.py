# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

numer = int(input("Введите номер билета: "))

num1 = numer // 1000
num2 = numer % 1000

n = num1 // 100
m = num1 // 10 % 10
k = num1 % 10

i = num2 // 100
j = num2 // 10 % 10
h = num2 % 10

if (n + m + k)==(i + j + h):
    print("Счастливый билет!")
else:
    print("Обычный")