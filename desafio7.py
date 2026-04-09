print('Calculadora de juros simples')
# mensagem que diz a função do programa

def calcular_juros(capital, taxa, tempo):
# define uma função para calcular juros simples, com capital sendo o dinheiro inicial, taxa sendo a porcentagem de juros e o tempo sendo o tempo em meses

    juros = (capital * taxa * tempo) / 100
# aplicação da fórmula de juros simples

    return juros
# retorna o valor calculado para quem chamou a função


def main():
    print("=== Cálculo de Juros Simples ===")
# define a função principal do programa e print mostra o título

    # Entrada de dados
    capital = float(input("Digite o capital (C): "))
    taxa = float(input("Digite a taxa de juros ao mês (I %): "))
    tempo = int(input("Digite o tempo em meses (T): "))
#  pede os dados para o usuário e converte para número decimal

    juros = calcular_juros(capital, taxa, tempo)
#  chama a função e guarda o resultado

    print(f"Juros calculados: R$ {juros:.2f}")
#  mostra o resultado com duas casa decimais


if __name__ == "__main__":
    main()
#  executa o programa

print('Até mais!')
# mensagem final
