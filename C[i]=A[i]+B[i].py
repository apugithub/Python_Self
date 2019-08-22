n = int(input())
arrayA = input().split()
arrayB = input().split()
arrayC = []
for i in range(n):
    arrayC.append(int(arrayA[i]) + int(arrayB[i]))
    print(int(arrayA[i]) + int(arrayB[i]))
print(' '.join([str(i) for i in arrayC]))
