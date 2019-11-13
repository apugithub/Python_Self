planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

planets [:2] = ["san","tanu", "Hello", "now" ] #Pay attention, first two position of the array will be filled by
               #all 4 elements, as list is mutable by nature]
print(planets)

print(planets[-1:-2])   # This will not give any o/p as the traverse can't be done reverse, its always from left to right
print (planets[-2:-1])  # So this one will return result
print(sorted(planets))
print(planets[1:-1])  # This will show all the planets except first and last one
numbs = [3,4,5]
a ='san'
print(sum(numbs))
print(planets.index('Mars'))
print(a in planets)  # Nice feature....boolean. return TRUE if a is in Planets
print(planets[-1])

'''

# Example 1
#Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that.
#These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.  Complete the function below to select the **captain** of the worst team.

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return(teams[(len(teams)-1)][1])
    pass
#################################################################

#Example 2:

# A guest is considered 'fashionably late' if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far)
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']


def fashionably_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

def test (arrivals, name):
    if arrivals.index(name) >= len(arrivals)/ 2 and arrivals.index(name) != len(arrivals)-1:
        print("Fashionably Late")


fashionably_late(party_attendees, 'Mona')

========================================================================================================

'''




