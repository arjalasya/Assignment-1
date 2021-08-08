n = int(input("No.of terms : "))
a = 0
b = 1
i = 0
print("The fibonacci series is ")
while i < n:
    print(a,end=' ')
    c = a+b
    b = a
    a = c
    i += 1
    
