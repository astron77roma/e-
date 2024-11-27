#Словарь
name="Словарь:"
print(name)
my_dict = {"Роман":1886,"Илья":2005,"Валерий":4589}
print(my_dict)
print(my_dict.get("Роман"))
print(my_dict.get("Николай"))
my_dict.update({"Сергей":2546,"Инна":6239})
print(my_dict)
my_dict.pop("Валерий")
print(my_dict)

#Множество
name="Множество:"
print(name)
my_set = {1,5,7,89,44,1,1,True,(2,3224,),True}
print(my_set)
my_set.add(False)
my_set.add(98)
print(my_set)
my_set.discard(1)
print(my_set)