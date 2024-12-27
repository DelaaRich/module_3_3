values_list = [1, "str", False]
values_dict = {"a":123,"b":"321","c":True}
values_list_2 = [54.32, "'Строка'" ]
def print_params (a = 1, b = 'строка',c = True):
    print(a,b,c)
print_params(*values_list_2, 42)