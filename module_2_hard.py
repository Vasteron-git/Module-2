
list_1 = []
list_2 = []
dict_1 = {}
for i in range(3, 21):
    list_1.append(i)
for i in range(1, 21):
    list_2.append(i)
for i in range(3, 21):
    for j in range(1, i):
         for k in range(0, i):
            if j  + list_2[j + k] > i:
                break
            if i % (j + list_2[j + k]) == 0:
                if dict_1.get(i):
                    dict_1[i] = dict_1.get(i) + str(j) + str(list_2[j + k])
                else: dict_1[i] = str(j) + str(list_2[j + k])
for i in range(3, len(dict_1) + 3):
    print(str(i) + " - " + dict_1[i])