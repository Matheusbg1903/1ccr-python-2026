print("ola mundo")

print(7+4)
print('7+4')
print('7'+'4') # CONCATENAÇÃO DE STRINGS

# Comentários de uma linha
'''
    Comentários de 
    multíplas
    linhas
    Autor: Matheus Borges
    Versão: 1.0.1
'''

# VARIÁVEIS
nome = 'Matheus Borges'    # string
idade = 20                 # int
peso = 67.2                # float

print(nome, idade, peso)
print(f"Oiiii, {nome}!!!")

# INPUT - SIMULAÇÃO DE FORMS NO CMD
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 2007
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"Sua idade é: {idade}")
