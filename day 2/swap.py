#1
a = 10
b = 15
a,b = b,a      # swap without using a third variable
print("a =", a)
print("b =", b)
#2
x = 20
y = 10

x = x + y 
y = x - y
x = x - y 
print("x =",x)
print("y =",y)