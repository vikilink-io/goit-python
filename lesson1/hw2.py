a = input ('Please enter a')
b = input ('Please enter b')
c = input ('Please enter c')
a = int(a)
b = int(b)
c = int(c)
D = b**2 - 4*a*c
x1 = (-b + D*0.5) / (2*a)
x2 = (-b - D*0.5) / (2*a)
x1text = f"x1={x1}"
x2text = f"x2={x2}"
print (x1text)
print (x2text)
