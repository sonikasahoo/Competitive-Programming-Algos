import tkinter
from tkinter import messagebox

def Sum():
    num1=eval(n1.get())
    num2=eval(n2.get())
    res=num1+num2
    messagebox.showinfo("Addition",res)

def Diff():
    num1=eval(n1.get())
    num2=eval(n2.get())
    res=num1-num2
    messagebox.showinfo("Subtraction",res)

def mult():
    num1=eval(n1.get())
    num2=eval(n2.get())
    if(num1!=0):
        res=num1*num2
        messagebox.showinfo("Product",res)
    else:
        messagebox.showinfo("Product","0")

def div():
    num1=eval(n1.get())
    num2=eval(n2.get())
    if(num2==0):
        messagebox.showinfo("Division","Error")
    elif(num1==0 and num2!=0):
        messagebox.showinfo("Division","0")
    else:
        res=num1/num2
        messagebox.showinfo("Division",res)

def pi():
    num1=eval(n1.get())
    num2=eval(n2.get())
    res=num1*num2*3.14
    messagebox.showinfo(" Pi ",res)

def percentage():
    num1=eval(n1.get())
    res=num1/100
    messagebox.showinfo(" Percentage ",res)

def sqr():
    num1=eval(n1.get())
    res=num1**2
    messagebox.showinfo(" Square ",res)

def cube():
    num1=eval(n1.get())
    res=num1**3
    messagebox.showinfo(" Cube ",res)

def power():
    num1=eval(n1.get())
    num2=eval(n2.get())
    res=pow(num1,num2)
    messagebox.showinfo(" Power ",res)

def sqrroot():
    num1=eval(n1.get())
    res=num1**0.5
    messagebox.showinfo(" Square ",res)

def cuberoot():
    num1=eval(n1.get())
    res=num1**(1/3)
    messagebox.showinfo(" Cube ",res)

def powerroot():
    num1=eval(n1.get())
    num2=eval(n2.get())
    res=pow(num1,(1/num2))
    messagebox.showinfo(" Power ",res)

def byx():
    num1=eval(n1.get())
    res=1/num1
    messagebox.showinfo(" output ",res)

def fact():
    num1=eval(n1.get())
    f=1
    for i in range(num1,0,-1):
        f*=i
    messagebox.showinfo(" Cube ",f)

def exponential():
    num1=eval(n1.get())
    res=pow(2.7182,num1)
    messagebox.showinfo(" Cube ",res)

root=tkinter.Tk()

l1=tkinter.Label(root,text="Enter 1st number : ")
l2=tkinter.Label(root,text="Enter 2nd number : ")
n1=tkinter.Entry(root)
n2=tkinter.Entry(root)

b1=tkinter.Button(root,text="   +   ",command=Sum)
b2=tkinter.Button(root,text="   -   ",command=Diff)
b3=tkinter.Button(root,text="   *   ",command=mult)
b4=tkinter.Button(root,text="   /   ",command=div)
b5=tkinter.Button(root,text="   %   ",command=percentage)
b6=tkinter.Button(root,text="   pi   ",command=pi)
b7=tkinter.Button(root,text="   x^2   ",command=sqr)
b8=tkinter.Button(root,text="   x^3   ",command=cube)
b9=tkinter.Button(root,text="   x^y   ",command=power)
b10=tkinter.Button(root,text="sqrroot(x)",command=sqrroot)
b11=tkinter.Button(root,text="cuberoot(x)",command=cuberoot)
b12=tkinter.Button(root,text="y^(1/x)",command=powerroot)
b13=tkinter.Button(root,text="1/x",command=byx)
b14=tkinter.Button(root,text="x!",command=fact)
b15=tkinter.Button(root,text="e^x",command=exponential)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

n1.grid(row=0,column=1)
n2.grid(row=1,column=1)

b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=3,column=0)
b5.grid(row=3,column=1)
b6.grid(row=3,column=2)
b7.grid(row=4,column=0)
b8.grid(row=4,column=1)
b9.grid(row=4,column=2)
b10.grid(row=5,column=0)
b11.grid(row=5,column=1)
b12.grid(row=5,column=2)
b13.grid(row=6,column=0)
b14.grid(row=6,column=1)
b15.grid(row=6,column=2)

root.mainloop()
