try:
    valor = float(input("Digite o valor do produto:"))
    qtd = int(input("Digite a quantidade de produtos:"))
    total = valor * qtd
    print("Total: ", total)
except ValueError:
    print("Erro! Valor inserido inválido!")
