rows = int(input("Enter the no.of lines "));
spaces = rows-1
for i in range(0,rows):
    for j in range(0,spaces):
        print(end=" ")
    spaces=spaces-1
    for j in range(0,i+1):
        print(" * ",end="")
    print(" ")
