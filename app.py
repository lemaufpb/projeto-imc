
# Programa IMC
nome = input("Qual é o seu nome? \n")
peso = input("Informe seu peso: \n")
altura = input("Informe sua altura: \n")

# Converter variáveis e calcular o IMC
imc = float(peso)/float(altura)**2

# Imprimir o resultado
print(f"Olá {nome}! Seu IMC é {imc:.2f}")
