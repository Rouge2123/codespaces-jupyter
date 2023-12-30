
print("Boolean")
print(True + False)
print(True - False)
print(True + True)
print(True - True)
print(False + False)
print(False - False)

print(""); print("Int")
print(3 + 5)
print(3-5)

print(""); print("Str")
print("Hello" + "How are you?")
# print("Hello" - "How are you?")

print(""); print("Float")
print(1.543 + 1.543)
print(1.543 - 1.543)

print(""); print("Mix")
# print(3 + "Hello") # Plus and minus doesn't work when mixing Int and Str
print(3 + True) # True = 1
print(3 + False) # False = 0
# print("Hello" + True) # Typeerror, 

menge = {0,1, 2, True, "s"}
menge2 = {0,1, 2, 3, True, "s"}

print(menge)
print(menge - menge2)

l = [1,'a',5,1,2,5]
print(l)
print(set(l))
print(l+l)
