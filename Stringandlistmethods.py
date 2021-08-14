#String methods
s1="string and list METHODS"
string1 = "   this is a Mycaptain assignment.List and string methods.   "
string2 = "s\tt\tr\ti\tn\tg\t "
tup = ("My", "Captain", "Assignment")
dict1 = {77: 109}
string3 = "This is a task to submit through\n google forms"
string4 = "We used {}"

print("The below are changes in the alphabets in the string .............")
print("Use of capitalize(first letter capital)                             ---",s1.capitalize())
print("Use of upper                                                        ---",s1.upper())
print("Use of lower                                                        ---",s1.lower())
print("Use of casefold                                                     ---",s1.casefold())
print("Use of swapcase                                                     ---",s1.swapcase())
print("Use of translate(use dict unicode values and make changes in string)---",string1.translate(dict1))
print("Use of replace                                                      ---",string1.replace("assignment", "Assignment"))
print("Use of title(first of every word caps)                              ---",string1.title())
print("Use of zfill                                                        ---",string2.zfill(10))
print("Use of join                                                         ---"," ".join(tup))


print("The below are the true or false output methods............")
print("Use of isupper                                                      ---",string1.isupper())
print("Use of islower                                                      ---",string1.islower())
print("Use of isdigit                                                      ---",string1.isdigit())
print("Use of isalnum                                                      ---",string1.isalnum())
print("Use of isalpha                                                      ---",string1.isalpha())
print("Use of isdecimal                                                    ---",string1.isdecimal())
print("Use of isidentifier                                                 ---",string1.isidentifier())
print("Use of isnumeric                                                    ---",string1.isnumeric())
print("Use of isspace                                                      ---",string1.isspace())
print("Use of istitle                                                      ---",string1.istitle())
print("Use of endswith                                                     ---",string1.endswith("e"))
print("Use of find                                                         ---",string1.find("a"))
print("Use of startswith                                                   ---",string1.startswith("T"))
print("Use of isprintable                                                  ---",string2.isprintable())


print("The below gives the index or no.of times the letter occurred...")
print("Use of center                                                       ---",string1.center(20))
print("Use of count                                                        ---",string1.count("i"))
print("Use of index                                                        ---",string1.index("Mycaptain"))


print("These are the normal strips and also left and right strips....")
print("Use of ljust(count from index 0 and prints \"end\" at 49th position)  ---",s1.ljust(50),"end")
print("Use of rjust(count from index 0 and prints \"s1\" at 49th position)   ---",s1.rjust(50),"end")
print("Use of lstrip                                                       ---",string1.lstrip(),"end")
print("Use of rfind                                                        ---",string1.rfind("s"))
print("Use of rindex                                                       ---",string1.rindex("and"))
print("Use of rpartition                                                   ---",string1.rpartition("Mycaptain"))
print("Use of rsplit                                                       ---",string1.rsplit("."))
print("Use of rstrip                                                       ---",string1.rstrip(),"end")
print("Use of expandtabs                                                   ---",string2.expandtabs(5))
print("\n")

print("These replace or part the strings elements...................")
a = string1.maketrans("M","m")
print("Use of maketrans and translate                                      ---",string1.translate(a))
print("Use of partition                                                    ---",string1.partition("Mycaptain"))
print("Use of split                                                        ---",string1.split())
print("Use of splitlines                                                   ---",string3.splitlines())


print("\n")
print("These are the format and encode methods.............\n")
encoded = string1.encode(encoding='UTF-8', errors='strict')
print("Use of encode                                                       ---",encoded)
print("Use of decode                                                       ---",encoded.decode(encoding='UTF-8',errors='strict'))
print("Use of format                                                       ---",string4.format("a format specifier here."))
print("Another use of format specifier  {} ; {}                               ".format(s1,string1))




#list methods

l1 = ["Mycaptain", "Assignment", "Github","Github"]
l2 = ["Lists", "Strings", "Tuples", "Dictionary", "Sets"]

l1.append("String and List Methods")
print("Usage of append",l1)
l1.reverse()
print("Usage of reverse",l1)
b=l1.count("Github")
print("Usage of count",b)
l1.copy()
print("Usage of copy",l1)
l1.extend(l2)
print("Usage of extend",l1)
a=l1.index("Mycaptain")
print("Usage of index",a)
l1.insert(4,"Upload")
print("Usage of insert",l1)
l1.pop(2)
print("Usage of pop",l1)
l1.remove("Mycaptain")
print("Usage of remove",l1)
l1.sort()
print("Usage of sort",l1)
l1.clear()
print("Usage of clear",l1)
