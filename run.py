
a1='y'
while a1=='y':
    filename=input("Enter name of file with extension:")
    path="D:\\CS\\"
    obj=path+filename
    p1=open(obj,"w")
    w1=input("Enter sentence you want to overwrite:")
    p1.write(w1)
    p1.close()
    print("Your  contents are weritten to the file")

    a2=input("Do you want to read it? ::yes/no")
    if a2=='yes':
        b1=open(obj,"r")
        s1=b1.read()
        print(s1)
        b1.close()

    a1=input("Do you want to create new file? ::y/n")


