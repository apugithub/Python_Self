a = int(input("Enter the value : \n"))


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(a))
