print('Bem vindo ao programa que lista o nome de 5 pessoas') 
# Mostra uma mensagem explicando o objetivo do programa.

nomes = []
# Cria uma lista vazia chamada nomes, que vai guardar os nomes e o usuário digitar

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
# range(5) significa que o loop vai rodar 5 vezes e i começa em 0 e vai até 4 (0, 1, 2, 3, 4)

    nomes.append(nome)
# .append() serve para inserir um item no final da lista

print("\nLista de nomes digitados:")
# Mostra um título antes de exibir a lista.\n pula uma linha para deixar mais organizado

for nome in nomes:
    print(nome)
# A variável nome vai assumir cada valor da lista e print(nome) imprime cada nome da lista

print( 'Aqui está a lista ! Até mais' )
# mensagem final
