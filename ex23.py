continuar = True
somaNotas = 0.0
qtdAprovados = 0
qtdRecuperacao = 0
qtdReprovados = 0

informacoesAlunos = []

def classificar(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota < 7 and nota >= 5:
        return "Recuperação"
    elif nota < 5:
        return "Reprovado"

while continuar:
    try:
        nome = input("\nDigite o nome do aluno:")
        idade = int(input("Digite a idade do aluno:"))

        if idade <= 0:
            while idade <= 0:
                print("Erro! Idade deve ser maior que 0.")
                idade = int(input("\nDigite a idade do aluno:"))

        nota = float(input("Digite a nota do aluno:"))

        if nota < 0 or nota > 10:
            while nota < 0 or nota > 10:
                print("Erro! Nota deve ser um valor entre 0 e 10.")
                nota = float(input("\nDigite a nota do aluno:"))

        situacao = classificar(nota)

        if situacao == "Aprovado":
            qtdAprovados += 1
        elif situacao == "Recuperação":
            qtdRecuperacao += 1
        elif situacao == "Reprovado":
            qtdReprovados += 1

        informacoesAlunos.append({"Nome": nome, "Idade": idade, "Nota": nota, "Situacao": situacao})
    except ValueError:
        print("Erro! Valor inválido inserido.\n")

    opcao = input("Deseja continuar? (S/N)")
    if opcao.lower() == "s":
        continuar = True
    else:
        continuar = False

def calcularMedia(soma, alunos):
    mediaSala = soma/alunos
    return mediaSala

for i in range(0, len(informacoesAlunos)):
    somaNotas += informacoesAlunos[i]["Nota"]

print("\nInformações:")
for i in range(0, len(informacoesAlunos)):
    print("Nome:", informacoesAlunos[i]["Nome"], "Situação:", informacoesAlunos[i]["Situacao"])

print ("\nMédia da sala:", calcularMedia(somaNotas, len(informacoesAlunos)))

print("\nQuantidade de alunos aprovados:", qtdAprovados)
print("Quantidade de alunos em recuperação:", qtdRecuperacao)
print("Quantidade de alunos reprovados:", qtdReprovados)

nomeMaiorNota = ""
maiorNota = 0
nomeMenorNota = ""
menorNota = 10

for i in range(0, len(informacoesAlunos)):
    if informacoesAlunos[i]["Nota"] > maiorNota:
        maiorNota = informacoesAlunos[i]["Nota"]
        nomeMaiorNota = informacoesAlunos[i]["Nome"]
    if informacoesAlunos[i]["Nota"] < menorNota:
        menorNota = informacoesAlunos[i]["Nota"]
        nomeMenorNota = informacoesAlunos[i]["Nome"]

print("\nAluno com a maior nota:", nomeMaiorNota,". Nota:", maiorNota)
print("Aluno com a menor nota:", nomeMenorNota,". Nota:", menorNota)