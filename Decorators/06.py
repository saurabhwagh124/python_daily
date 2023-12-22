def sum_it(*argv):
    sum = 0
    for i in argv:
        sum = sum+i
    return sum

print(sum_it(21,24,52))

