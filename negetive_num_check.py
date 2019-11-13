
# Negetive number check
def check(num):
    return True if (num<0) else False

print(check(-2))


### The function does check and return the negatives from a list

lst = [4,-5,4, -3, 23, -254]

def neg(lst):
    return [num for num in lst if num <0]
    # or the above statement can be written as=   return sum([num < 0 for num in nums])

print(neg(lst))