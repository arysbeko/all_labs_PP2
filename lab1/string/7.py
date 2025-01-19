#1
x = "Hello World"
print(x)

#2
txt = "Hello World"
x = txt[0]
print(x)    #H

#3
txt = "Hello World"
x = txt[2:5]
print(x)    #llo

#4
txt = "   Hello World   "
x = txt.strip()
print(x)    #Hello World

#5
txt = "Hello World"
txt =txt.upper()
print(txt)    #HELLO WORLD

#6
txt = "Hello World"
txt=txt.lower()
print(txt)     #hello world

#7
txt = "Hello World"
txt=txt.replace("H","J")
print(txt)     #Jello World

#8
age=17
txt = "My name is Bek, and I am {}"
print(txt.format(age))    #My name is Bek, and I am 17