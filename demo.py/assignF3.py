dict1 = {
    "english" : 23,
    "maths" : 34,
    "history" : 45,
    "geography" : 57

}

dict2 = {
    "python" : 23,
    "java" : 48,
    "dsa" : 34,
    "maths" : 58
}

result = dict1.copy()
for key, value in dict2.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value
print(result)            