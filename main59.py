a = int(input('Введи трицифрове число: '))

s = str(a) #число в рядок
digits = list(map(int, s)) #символ у число
result = sum(digits) #сумма цифр

print(result)
