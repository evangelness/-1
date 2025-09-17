a = int(input())  # олівці
b = int(input())  # ручки
c = int(input())  # фломастери
d = int(input())  # ціна олівця

pen_price = d + 2
marker_price = d + 9

total = a * d + b * pen_price + c * marker_price

print(total)