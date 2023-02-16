x =int(input("Digite o valor de x"))
y =int(input("Digite o valor de y"))
z =int(input("Digite o valor de z"))

if x > y and x > z:
    result = "x ´e o maior número"
elif y > x and y > z:
    result = "y é o maior número"
elif z > x and z > y:
    result = "z é o maior"
else:
    result = "há números iguais"
    
print(result)