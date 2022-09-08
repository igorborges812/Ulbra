valor = int(input("Digite um valor R$: "))

#Quantidade de notas de 100
a = valor // 100
a2 = valor % 100

#Quantidade de notas de 50
b = a2 // 50
b2 = a2 % 50

#Quantidade de notas de 20
c = b2 // 20
c2 = b2 % 20

#Quantidade de notas de 10
d = c2 // 10
d2 = c2 % 10

#Quantidade de notas de 5
e = d2 // 5
e2 = d2 % 5

#Quantidade de notas de 2
f = e2 // 2
f2 = e2 % 2

#Quantidade de notas 1
g = f2 // 1

print("O valor digitado foi R$: ", valor)
print("Relação de Notas Necessárias: ")
print(a, 'nota(s) de 100')
print(b, 'nota(s) de 50')
print(c, 'nota(s) de 20')
print(d, 'nota(s) de 10')
print(e, 'nota(s) de 5')
print(f, 'nota(s) de 2')
print(g, 'nota(s) de 1')