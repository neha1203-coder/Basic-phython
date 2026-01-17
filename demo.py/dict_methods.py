languages = {
"p1" : "C",
"p2" : "C++",
"p3" : "JavaScript",
"p4" : "Python",
"p5" : "Java"

}
print(languages)
print(languages.keys())                    # returns all keys
print(languages.values())                  # returns all values
print(list(languages.values()))            # typecasting convert dict into list we can also convert list into dict
print(languages.items())                  # returns all (key, cal) pairs as tuples
pairs = list(languages.items())
print(pairs[1])                             #it returns value at 1st index
print(languages["p1"])                     #it also returns values 
#print(languages["p11"])                    # it gives error
print(languages.get("p1"))                # returns the key according to value
#print(languages.get("p11"))               #it returns none in the output
languages.update({"p6":"html"})              # insert the specified items to the dictionary
print(languages)                