#6 Faça um programa que solicite ao usuário sua idade, depois disso,
#exiba a classificação etária de acordo com as faixas de valores:
 
idade = int(input("Digite sua idade: "))


if idade <= 11:
    print("Classificação Etária: Infantil")
elif idade <= 17:
    print("Classificação Etária: Adolescente")
elif idade <= 59:
    print("Classificação Etária: Adulto")
else:
    print("Classificação Etária: Idoso")