
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [10, "Hello", False]
values_dict = {'a' : 50, 'b' : "parameter", 'c' : False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ["parameter2", False]
print_params(*values_list_2, 42)