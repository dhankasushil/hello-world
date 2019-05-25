import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York" , "bhai" : ["b","c","d"] }'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:

del y["bhai"]

# print(y)

x=json.dumps(y, indent=2, sort_keys=True);

print(x)



# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# y=json.dumps(x)

# print(y[5])