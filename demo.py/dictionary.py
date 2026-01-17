info = {
    "key" : "value",  # string values
    "name" : "neha",        # string values
    "learning" :"python",      # string values
    "age" : 29,                # integer value
    "is_adult" : True,       # boolean value
    "marks" : 49.23,        # float values
    "subject list" : ["python","java","c++"],     # given is in the form of list
    "topics" : ("dictionary", "set"),             # given is in the form of tuples
     34 : 43                                      # we can take inter value as a key also we can take bollean tuples as a key as well as value                                 
}
#print(info)
print(type(info))
print(info["name"])                                # we can access any key and values induvidually
print(info["age"])
print("lenght of info",len(info))
info["name"] = "neha kumari"                       # dictionaries are mutable we can change the value of keys at runtime
info["age"] = 22
info["surname"]  = "sinha"                          # we can also add key and value after dcitionaries declaration
print(info)
null_dict = {}                                      # null dictionary with no keys and value
print(null_dict)
