'''tax = 12.5 / 100
price = 100.50
print (price * tax)
print (tax-price)'''

'''import numpy as np
print(np.arange(start=1, stop=10, step=3))
print (np.arange(1,10,1))'''

'''a, b = 0, 10
while (a<5):
    print (b, end=',')
    a=a+1'''

'''x = (input("Enter the string \n"))
print(x)'''
'''x = int(input("San\n"))
print(x)'''

'''import math
print(math.sin(30))
print(math.cos(10))
print(int(math.pow(11,11)))'''

'''a, b = 10, 22  # If and elif loop
if (a>b):
    print("a is less than b")
elif(b>50):
    print("b is greater than 5")
else:
    print ("default")'''

'''words = ['London', 'Dhaka', 'Seol', 'Santiago']
for i in range(4):
    print (words[i])
    #for j in i:
        #print(j, len(i))'''

'''a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i+1, a[i])'''

'''def abg (var1, var2=100, var3="San"):
    print("var1= ", var1, "var2= ", var2, "var3= ", var3)

print(abg(343,var3="Manu", var2=777))'''

'''a= "Santanu"
print(a.upper())'''

#items = ["Microphone", "Phone", 5502.22, "Camera", 312.33, "Cliff Bars", 423.00]
##############################################################
'''def lambda_test(a,b):
    return  lambda a, b: a+b

f = lambda_test(100,65)
print(f(2,4))'''

'''r = lambda a,b: a+b
print (r(4,3))'''
########################################################
'''def my_func1():
    "nsjkbvsjb"
    pass
print(my_func1.__doc__)'''


'''fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.insert(2,"UP")
print(fruits)
fruits.remove("UP")
print(fruits)
print(fruits.index("pear"))
fruits.sort(reverse=True)
print(fruits)
print(fruits.count("apple"))
del fruits[1]
print(fruits)'''

##print((lambda x,y: x + y)(2,3))


the_dict = {
    "Name" : "Blood Diamond",
    "Actor" : "Leonardo",
    "Year" : 2007,
    "IMDB" : 6.1,
}
print(the_dict.get("Name"))
print(the_dict["Actor"]+"\n")

for x in the_dict :
    print(the_dict[x])

for x,y in the_dict.items() :
    print (x,y)







