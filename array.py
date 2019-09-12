'''
a = []
s = [77,'9',"San",4.78]

for i in range(len(s)):
    a.append(i)
print (a)  # This will append all the elements from s[] to a[]

for j in range(len(s)):
    print("The %i th element is: " %j, s[j])  # Traversing List
'''
#program to create an array of 5 integers and display the array items
import array as ar

a = ar.array('i', [34,44,12,46, 62])
print (type(a))

for i in range(len(a)):
    print ("The %i th element is : " %(i+1), a[i])  # Traversing array elements

#  Program to append a new item to the end of the array
a.append(67)
print(a)

# program to reverse the order of the items in the array
a.reverse()
print(a)


print.count(a)












