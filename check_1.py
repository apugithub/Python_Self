import time
start = time.time()
a = ['uiy', 'ODS', 'kjk', 'jhg']

print(len(a))


def fw(**kargs):
    print(kargs['ar'])
    if len(kargs['ar']) > 5:
        print('length not great')

    elif 'ODS' in [i.upper() for i in kargs['ar']]:
        print('ods is not present')

    else:
        print('finally at else')


fw(ar=a, br=a)

end = time.time()
# print('\nExecution time: {} seconds'.format(end-start))
