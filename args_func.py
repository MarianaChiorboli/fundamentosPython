# valores dentro de função = parametros 

# 1 - Imprime um nome completo

def full_name(first_name, last_name):
    print(f"Nome: {first_name} Sobrenome: {last_name}")

full_name("Mari", "Chiorboli") #na hora de chamar a função, passar os "parametros" dentro do paranteses

# 2 - função para somar dois numeros

def sum_numbers(numA, numB):
    return numA + numB

print(f"Soma dos números = {sum_numbers(7, 4)}")

# 3 - função com parametros default
def address(country = "Brasil"): # já defini o parametro diretamente na função 
    print(f"Eu moro em: {country}")

address()
address("Portugal") #sendo atualizado

#4 - função para avaliar o filme
def rate_movie(movie_name, num_ratings):
    total = 0
    for i in range(num_ratings):
        note = float(input("Digite a nota para o filme: "))
        total += note
    if num_ratings > 0:
        average = total / num_ratings
    else:
        average = 0

    print(f"Média de avaliação do filme: {movie_name} é {average}")

rate_movie("frozen", 2)