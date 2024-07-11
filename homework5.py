immutable_var = 1, 2, 'string', True
print('Immutable tuple:',immutable_var) #элементы кортежа нельзя изменить, тк кортеж не поддерживает обращение по элементам
#immutable_var[0] = 5
mutable_list = [3, 4, 'sonya', False]
mutable_list[0] = 8
print('Mutable list:',mutable_list)