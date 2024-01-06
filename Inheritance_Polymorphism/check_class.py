class Demo:
    pass
print(dir(object))
print(dir(type))
# Type class has extra methods such as dict, module, weakref and operator methods
# and each class in python3 has same structure as type class
# but not in case of python2
print(dir(Demo))
