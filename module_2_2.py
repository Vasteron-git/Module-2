
first = int(input("Введите число first: "))
second  = int(input("Введите число second: "))
third  = int(input("Введите число third: "))

if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)




