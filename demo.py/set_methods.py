marks = {43,53,86,23,94}
marks1 = {32,43,66,72}
marks.add(53)                #add an elements
print(marks)                # in sets elements add randomly
marks.remove(94)            # removes the element
print(marks)
print(marks.pop())               # remove a random value
print(marks.pop()) 
print(marks.union(marks1))    # combines both set values and returns new
print(marks.intersection(marks1))      # combines common values and returns new
marks.clear()               # empties the set
print(marks)