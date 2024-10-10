print("Введите пятизначное число :")

n = float(input())
ones = int(n % 10)
tens = int(n % 100 / 10)
hundreds = int(n % 1000 / 100)
thousands = int(n % 10000 / 1000)
tens_of_thousands = int(n % 100000 / 10000)

print("Единицы: ", ones)
print("Десятки: ", tens) 
print("Сотни: ", hundreds) 
print("Тысячи: ", thousands) 
print("Десятки тысяч: ", tens_of_thousands) 

print("Результат :", float(tens ** ones * hundreds / (tens_of_thousands - thousands)))