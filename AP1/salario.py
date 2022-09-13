num_funcionario = float(input("Digite seu número de funcionário: "))
horas_trabalhadas = float(input("Digite suas horas trabalhadas: "))
val_ph = float(input("Digite quanto você recebe por hora: "))
filhosM14 = int(
    input("Digite o numéro de filhos menores de 14 anos que você possui: "))
idade = int(input("Digite sua idade: "))
temp_servico = float(input("Digite o seu tempo de serviço: "))
sal_familia = float(input("Digite o valor recebido pelo salário familia: "))

salario = (horas_trabalhadas * val_ph) * 25
desc_inss = salario * 0.085
sal_familia_total = sal_familia * filhosM14
sal_bruto = salario + sal_familia_total

if sal_bruto > 1.500:
    imposto_renda = sal_bruto * 0.15

elif sal_bruto > 500 and sal_bruto <= 1500:
    imposto_renda = sal_bruto * 0.08

else:
    imposto_renda = sal_bruto

total_desc = desc_inss + imposto_renda
sal_liquido = sal_bruto - total_desc

print("O seu número de funcionário é: ", num_funcionario)
print("O seu salário bruto é: ", sal_bruto)
print("O total de descontos é: ", total_desc)
print("O salário liquido é: ", sal_liquido)
