#1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


#2
x = thisdict.get("model")
# If the key is absent, Thisdict ["Model"] will cause an error, a .get () will return None.


#3
x = thisdict.keys()
print(x)  # dict_keys(['brand', 'model', 'year'])


#4
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change
# dict_keys(['brand', 'model', 'year'])

car["color"] = "white"

print(x) #after the change
# dict_keys(['brand', 'model', 'year', 'color'])


#5
x = thisdict.values()
# print(x)  # dict_values(['Ford', 'Mustang', 1964])

#6
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change
# dict_values(['Ford', 'Mustang', 1964])

car["year"] = 2020

print(x) #after the change
# dict_values(['Ford', 'Mustang', 2020])


#7
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change



#8
x = thisdict.items()
print(x)  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])



#9
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020), ('color', 'red')])


#10
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change



#11
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")