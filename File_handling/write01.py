fobj = open("Test2.txt","w")
#fobj.write("This\nis to\nwrite an example\n")
list1 = ["Line one\n",'Line two\n','Line3\n']
fobj.writelines(list1)
