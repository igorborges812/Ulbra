sexo = str(input("Digite o seu sexo, M para masculino e F para feminino: "))
altura = float(input("Digite a sua altura: "))

M = (72.7*altura)-58
F = (62.1*altura)-44.7

if sexo == "M":
    print("Seu peso ideal é: ", M)

else:
    print("Seu peso ideal é:", F)
