num1=int(input("Digite um valor: "))
num2=int(input("Digite outro valor: "))

par1=num1%2
par2=num2%2

soma=num1+num2

quad1=num1**2
quad2=num2**2

if par1 == 0:
    print("O primeiro valor digitado é par ")
else:
    print("O primeiro valor digitado é impar ")

if par2 == 0:
    print("O segundo valor digitado é par")
else: 
    print("O segundo valor digitado é impar ")
if num1 < 10:
    print("O primeiro valor digitado é menor que 10")
elif num1 == 10:
    print("O valor digitado é igual a 10 ")
else:
    print("O primeiro valor digitado é maior que 10")
if num2 < 10:
    print("O segundo valor digitado é menor que 10")
elif num2 == 10:
    print("O segundo valor digitado é igual a 10 ")
else:
    print("O segundo valor digitado é maior que 10")
print("O quadrado do primero valor é: ", quad1)
print("O quadrado do segundo valor é: ", quad2)
print("O resto da divisão do primeiro valor por 2 é: ", par1)
print("O resto da divisão do segundo valor por 2 é: ", par2)
print("A soma dos dois valores digitados é: ", soma)








