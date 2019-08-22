# This for loop will append all the int/float values and str values. Assuming that a list may have another list inside

items = [123, "San", 1234, "Tapan", 23.67, 34.78, 445]
item_2 = ["test", items]

str_test = []
num_test = []

for i in item_2:
    if isinstance(i, list):  # This if loop is used assuming the presence of list inside a list
        for j in i:
            if isinstance(j, int) or isinstance(j, float):
                num_test.append(j)
            elif isinstance(j, str):
                str_test.append(j)
            else:
                pass

    elif isinstance(i, int) or isinstance(i, float) :
        num_test.append(i)
    elif isinstance(i, str):
        str_test.append(i)
    else:
        pass


print(str_test)
print ('\n')
print(num_test)
print(item_2)
