planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets [:2] = ["san","tanu", "Hello", "now" ] #Pay attention, first two position of the array will be filled by
               #all 4 elements, as list is mutable by nature]
print(planets)

print(planets[-1:-2])   # This will not give any o/p as the traverse can't be done reverse, its always from left to right
print (planets[-2:-1])  # So this one will return result
print(sorted(planets))
print(planets[-5:-2])
numbs = [3,4,5]
a ='san'
print(sum(numbs))
print(planets.index('Mars'))
print(a in planets)  # Nice feature....boolean.






