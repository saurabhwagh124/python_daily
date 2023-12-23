def fun(x,y):
    print("Start fun")

    while(x<=y):
        yield x
        x = x+1
    print("End fun")
for val in fun(1,10):
    print(val)
# for works something different than the next() this not only return the yield code but also the later ones
