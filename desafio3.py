# Lista de 5 nomes com input e print

nomes = []

# Pedindo 5 nomes ao usuário
for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

# Imprimindo todos os nomes
print("\nLista de nomes digitados:")
for nome in nomes:
    print(nome)
