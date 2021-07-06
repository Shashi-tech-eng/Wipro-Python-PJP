dict3_UserID = {"k1" : 10,  "k2" : 20,  "k3" : 30}

# we get KeyError 
try:
    print(dict3_UserID["k5"])
except KeyError:
    print("Please Enter another key!")