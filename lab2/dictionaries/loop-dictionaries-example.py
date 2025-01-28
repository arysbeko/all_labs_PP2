thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#1
for x in thisdict:
    print(x)
# brand
# model
# year
   
#2
for x in thisdict:
    print(thisdict[x])
# Ford
# Mustang
# 1964

#3
for x in thisdict.values():
    print(x)
# Ford
# Mustang
# 1964

#4
for x in thisdict.keys():
    print(x)
# brand
# model
# year

#5
for x, y in thisdict.items():
    print(x, y)
# brand Ford
# model Mustang
# year 1964