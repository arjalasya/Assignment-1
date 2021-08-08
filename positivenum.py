n=int(input("Enter no.of elements in the list : "))
l1=[]
for i in range(0,n):
    a = int(input())
    l1.append(a)
print("The list is : ",l1)
l2=[]
for i in l1:
    if i>0:
        l2.append(i)
print("The positive integer are : ",l2)
