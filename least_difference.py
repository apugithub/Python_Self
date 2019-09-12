def least_difference (a,b,c):
    val1= abs(a-b)
    val2= abs(b-c)
    val3 = abs(c-a)
    print( min(val1,val2, val3))

least_difference(10, 56,1)
