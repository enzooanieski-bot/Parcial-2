
# juros_simples.py

def calcular_juros(capital, taxa, tempo):
    juros = (capital * taxa * tempo) / 100
    return juros


def main():
    print("=== Cálculo de Juros Simples ===")

    # Entrada de dados
    capital = float(input("Digite o capital (C): "))
    taxa = float(input("Digite a taxa de juros ao mês (I %): "))
    tempo = int(input("Digite o tempo em meses (T): "))

    # Cálculo
    juros = calcular_juros(capital, taxa, tempo)

    # Saída
    print(f"Juros calculados: R$ {juros:.2f}")


if __name__ == "__main__":
    main()
