#5 Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso,
#faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.   
ano_nascimento = int(input("digite o ano que vc nasceu:"))
 
from datetime import datetime
ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if idade >= 18:
    print("voce ja fez 18 anos, já pode ser preso")
else:
    print("voce ainda nao fez 18 anos")
