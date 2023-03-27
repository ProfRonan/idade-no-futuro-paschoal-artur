#Recebendo os dados do usuário
ano_atual = int(input("Digite o ano atual: "))
idade = int(input("Digite sua idade: "))
ano_qualquer = int(input("Digite um ano qualquer: "))
nome = input("Digite seu nome: ")

#Operação entre os anos específicados pelo usuário
anos = int(ano_qualquer - ano_atual)
operação = int(anos + idade)

#Exibindo valor de retorno para o usuário
print(str(nome) + ", " + "no ano de " + str(ano_qualquer) + " você terá " + str(operação) + " anos")