planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets [:2] = ["san","tanu", "Hello", "now" ] #Pay attention, first two position of the array will be filled by
               #all 4 elements, as list is mutable by nature]
print(planets)

print(planets[-1:-2])   # This will not give any o/p as the traverse cant be done reverse, its always from left to right
print (planets[-2:-1])  # So this one will return result

print(sorted(planets))

a = 10 + 3.34j
print (a.imag)



