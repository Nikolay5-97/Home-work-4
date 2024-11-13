mutable_list = [250, 380, False, "My name Nikolay", 1931]
mutable_list[2: 3] = 18, 31
print(mutable_list)

immutable_var = 1, 2, 3, True, "Hello , world"
print(immutable_var)
immutable_var [3] = False # - данные в кортеже неизменяемые
