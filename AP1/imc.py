peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))

imc = peso/altura**2 

print(imc)

if imc < 17:
    print("Seu IMC é:", imc , "e está classificado como MUITO ABAIXO DO PESO")
elif imc > 17 and imc < 18.49:
    print("Seu IMC é:", imc , "e está classificado como ABAIXO DO PESO")
elif imc >= 18.5 and imc < 24.99:
    print("Seu IMC é:", imc , "e está classificado como PESO NORMAL")
elif imc >= 25 and imc < 29.99:
    print("Seu IMC é:", imc , "e está classificado como ACIMA DO PESO")
elif imc >= 30 and imc < 34.99:
    print("Seu IMC é:", imc , "e está classificado como OBESIDADE I")
elif imc >= 35 and imc < 39.99:
    print("Seu IMC é:", imc , "e está classificado como OBESIDADE II")
else:
    print("Seu IMC é:", imc , "e está classificado como OBESIDADE III")