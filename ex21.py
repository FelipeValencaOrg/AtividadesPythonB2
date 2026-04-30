try:
    num1 = float(input("Digite um número:"))
    num2 = float(input("Digite outro número:"))
    soma = num1 + num2
    print(soma)
except ValueError:
    print("Erro! Valor inserido inválido!")
