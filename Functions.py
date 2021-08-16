s = str(input("Please enter a string "))
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    sort_dict = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for a in sort_dict:
        print(a[0],"=",a[1],end=" ")
    a=" "
    return a
print(most_frequent(s))
