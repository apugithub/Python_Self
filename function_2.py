# This function (sum_num) takes the numeric or float values and sum it up. Assuming a list will not have another list inside

items = [5, "San", 3, "Tapan", 2.5, 3, 4, 1]
#item_2 = ["test", items]

num_only = []

def sum_num (abc):
    total =0
    if isinstance(abc, list):
        for i in abc :
            if isinstance(i, int ) or isinstance(i, float):
                num_only.append(i)
            else:
                pass

    for j in num_only:
        total = total + j

    return total

def count_items (abc):  #This function count the total number of elements in a list.
    total = 0
    for i in abc:
        total = total + 1
    return total
    # This is similar to the len(items)


def sum_count_avg (abc):  # This func does the average, only condition is the list must contain only int or float
    total = 0
    count = 0
    for i in abc:
        if isinstance(i, int) or isinstance(i, float):
            total = total + i
            count = count + 1
        else:
            pass
    return("%.2f" % (total/count))   # This %.2f displays till 2 decimals.


print(sum_num(items))
print(count_items(items))
print (sum_count_avg(num_only))


