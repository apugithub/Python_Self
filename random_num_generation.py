import random as ra

#ra.seed(12)        #fixing seed means seeding the generators
for i in (range(1,3)):
    print('Random_%d=>'%i, ra.random())   #the default is to create random number (float) in between [0.0 - 1.0]

print ("\n")

for i in range(1,3):
    print('Random_(within range)_%d=>'%i, ra.uniform(2,3))   #this gives the random number (float) within specified range

print("\n")

for _ in range (3):  # look the variable i in for loop is not required.. if not used later
    print("Random number-Range(Int)_%d=>", ra.randint(10, 23))  # gives int number withing range,
    #randrange serves the same purpose as randint

print("\n")

a = [23, 43, 11, 87.1, 37, 5, 190]

for i in range(1,3):
    print("Randomly picked numbers_%d=>" %i, ra.choice(a) )  #randomly picks from a list

print("\n")

for i in range(1,3):
    print("Randomly picked numbers_%d=>" %i, ra.choices(a,k=2))

print("\n")


for i in range(1,4):
    ra.shuffle(a)  # This is meant to shuffle the list
    print("Just shuffling a list_%d=> " %i, a)
    #print("Just shuffling a list_%d=> " %i, ra.shuffle(a)) **** This would return nothing as shuffle()
    # function does not return a list.


