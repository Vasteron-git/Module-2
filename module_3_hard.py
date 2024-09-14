
def list_collect(symbol):
    if isinstance(symbol, tuple):
        for item in symbol:
            yield from list_collect(item)
    elif isinstance(symbol, list):
        for item in symbol:
            yield from list_collect(item)
    elif isinstance(symbol, dict):
        for key in symbol.items():
            yield from list_collect(key)
        # for value in symbol.items():
        #     yield from list_collect(value)
    elif isinstance(symbol, set):
        for item in symbol:
            yield from list_collect(item)
    else:
        yield symbol
def calculate_structure_sum(data_structure):
    list_ = list(list_collect(data_structure))
    sum = 0
    for i in range(0, len(list_)):
        if  type(list_[i]) == int:
            sum = sum + int(list_[i])
        else:
            sum = sum + len(list_[i])
    return sum
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)