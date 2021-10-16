#sorting dictionary in ascending order without using buil-in functions
d={}
c=int(input("Enter number of values : "))
while(c!=0):
    key=int(input("Enter key : "))
    val=int(input("Enter value : "))
    d[key]=val
    c-=1
d_asc={}
#low_key=0
print("Before sorting : ",d)
for i in range(len(d)-1):
    low=None
    for k in d:
        if low is None or (d[k]<low):
            low=d[k]
            low_key=k
    d_asc[low_key]=low
    d.pop(low_key,None)
d_asc.update(d)
print("sorted dictionary in ascending order : ",d_asc)
