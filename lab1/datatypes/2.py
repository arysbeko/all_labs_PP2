x=str("hello world")
x=int(20)
x=float(20.5)

x=complex(1j)
print(x)   #1j
print(type(x))  #<class 'complex'>

x=list(["apple","banana","cherry"])
print(x)

x=tuple(("apple","banana","cherry"))
print(x)

x=range(6)
print(x)   #range(0, 6)

x=dict(name="Bek",age=17)
print(x)   #{'name': 'Bek', 'age': 17}

x=set(("apple","banana","cherry"))
print(x)	#{'cherry', 'banana', 'apple'}

x = frozenset(("apple", "banana", "cherry"))
print(x)  #frozenset({'cherry', 'banana', 'apple'})

x=bool(5)
print(x)   #True

x=bytes(5)
print(x)   #b'\x00\x00\x00\x00\x00'

x=bytearray(5)
print(5)   #5

