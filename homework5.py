immutable_var  = (1, 2, 'coffe', 1 + 2j, True)
print(immutable_var)
# Попытайтесь изменить элементы кортежа immutable_var
# immutable_var[4] = False - кортеж не поддерживает обращение по элементам
print(immutable_var)
# в квадратных скобках это списки и их измнять можно
mutable_list = [1, 2, 'coffe', 1 + 2j, True]
mutable_list[4] = False
print(mutable_list)