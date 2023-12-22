def summing(**argv):
# here **argv means data is taken in form of dictionary
    sum=0
    for k,v in argv.items():
        sum=sum+v
    return sum
print(summing(x=1,y=99,z=21))
