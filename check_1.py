a = [1,2, 45]

try:
    a = int(a)
    print ('success')
except Exception as x:
    print(x)

try:
    with open("E:/hadoop/sample.json1", "r") as file:
        dict_file = file.readlines()
except Exception as x:
    print(x)

dct = {"filter":"1=1", "broadcast":"t1" }
print (dct)

if dct['filter'] == "1=1":
    dct['filter'] = ["1=1"]
print(dct["broadcast"])
