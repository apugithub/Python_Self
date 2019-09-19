# Boolean Test--


def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    #onion = True
    return not onion



def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    return (ketchup and mustard and onion)



def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return (( not ketchup) and (not mustard) and (not onion))
    #or
    # return not (ketchup or mustard or onion)



def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return  ketchup != mustard
    #the above line is same as below
    # return (ketchup and not mustard) or (mustard and not ketchup)
    # Can also be implemented by the int() function as below--
    # return int (ketchup + mustard) == 1



def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    # Here solving through boolean and , or , not is complicated, hence the int conversion is useful
    return (int(ketchup) + int(mustard) + int(onion)) == 1
    # the above line is same as below
    # return (ketchup + mustard + onion) == 1

