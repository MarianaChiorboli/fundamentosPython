#Função para imprimir mensagem
#Parenteses usado, pq pode ter um parametro (nesse caso não tem)
def welcome ():
    print("Bem-vindo!")

    #Com identação eu continuo dentro da função 
#welcome()

#Função para calcular a média de notas
def calculate():
    avaliacoes = int(input("Digite o número de avaliações a serem avaliadas: "))
    total = 0 #Váriavel de controle

    for i in range (avaliacoes):
        notas = float(input("Digite a nota da avaliação: "))
        total += notas

    if avaliacoes > 0:
        average = total / avaliacoes
    else:
        average = 0
    return average
#Em função temos duas possibilidades de saída, o retorno(não é apresentado na tela, dentro da função, apenas gera um retorno) ou o print

print(f"Média final das notas:  {calculate()}")