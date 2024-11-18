immutable_var = ([1,2,3],["a","b","c"])
print(immutable_var)
#immutable_var[0] = 1 #На выводе будет TypeError. Так как кортеж является неизменяемым типом данных, и не поддерживает обращение по элементам.
mutable_list = ["яблоко","груша", "банан"]
mutable_list.extend(["лимон", "вино"])
print(mutable_list)
