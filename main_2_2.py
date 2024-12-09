first = int(input("Введите Первое Число:"))
second = int(input("Введите Второе Число:"))
third = int(input("Введите Третье Число:"))
if first == second == third:
    print(3)
elif first == second or first == third or second == first:
    print(2)
else:
    print(0)
