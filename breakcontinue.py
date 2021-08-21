Characters=({"name":"Paul Wesley", "Age":39 , "Series":"The Vampire Diaries", "known as":"Stefan Salvatore"},
            {"name":"Ian Somerhalder", "Age":42 ,"Series":"The Vampire diaries", "Known as":"Damon Salvatore"},
            {"name":"Candice King", "Age":34 ,"Series":"The Vampire diaries", "Known as":"Caroline Forbes"},
            {"name":"Nina Dobrev", "Age":32 ,"Series":"The Vampire diaries", "Known as":"Elena Gilbert"},
            {"name":"Kat Graham", "Age":31 ,"Series":"The Vampire diaries", "Known as":"Bonnie Bennett"})
print("Using the break statement.......")
for i in range(0,len(Characters)):
    if i==2:
        break;
    else:
       print(Characters[i])
print("\n")
print("Using the continue statement......")
for j in range(0,len(Characters)):
    if j==2:
        continue;
    else:
        print(Characters[j])
