my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while len(my_list) != index:
    value = my_list.pop(0)
    if value > index:
        print(value)
    elif value == 0:
        continue
    else:
        break

