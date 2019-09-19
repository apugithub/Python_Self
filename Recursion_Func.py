item = [123, "San", 1234, "Tapan", 23.67, 34.78, 445]
item_2 = ["test", item]

str_test = []
num_test = []

def traverse_list (abc):
    if len(abc) == 0:
        print ("the list is empty")
    else:
        for i in abc:
            if isinstance(i, list):   #Means if there is list inside list
                traverse_list(i)
            else:
                if isinstance(i, int) or isinstance(i, float):
                    num_test.append(i)
                elif isinstance(i, str):
                    str_test.append(i)
                else:
                    pass
traverse_list(item_2)


print(str_test)
print ('\n')
print(num_test)
print(item_2)
