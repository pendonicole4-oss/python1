# open (filename,mode)
#mode - r-read,w-write,a-append,x-create
#write
x=open("demo.txt",'w')
x.write("This is python file handling")
x.close()
#append
y=open("demo.txt",'a')
y.write("\nThis is some appended text")
y.close()
#read
z=open("demo.txt",'r')
print(z.read())
z.close()
#x-create
file=open("trial.txt",'x')
file.write("Hello,Pendo!")
file.write("\nThis is python.")
file.close()

