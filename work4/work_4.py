# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

num = int(input("Введите число журавликов: "))

Kate = num // 2
Petya = Kate // 2
Sergey = Petya

print("Петя", Petya,',', "Катя", Kate,',', "Сергей", Sergey)