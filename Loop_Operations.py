'''
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end='')  # the word 'end' is used to print in a single line
'''
'''
s = 'hi There is another name in Background'
b = []

for i in s:
    if i.isupper():
        i = i.lower()
    b.append(i)

print(b)
print(s.capitalize())

squares = [2*n for n in range(10)]
print(squares)

'''
'''
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

short_planets = [planet for planet in planets if len(planet)==6]  # Additional if condition
print(short_planets)

shrt_planets = [planet.upper() + ' _Add This_'  for planet in planets if len(planet)==6]
print (shrt_planets)
'''

lst = [4,-5,4, -3, 23, -254]

def neg(lst):
    return ([num for num in lst if num <0])

print(neg(lst))