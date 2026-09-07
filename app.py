def calcular_consumo():
    print("=" * 45)
    print("  CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE  ")
    print("=" * 45)
    print()

    nome_aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ").strip()
    
    while True:
        try:
            potencia = float(input("Digite a potência do aparelho em Watts (W): "))
            if potencia > 0:
                break
            print("A potência deve ser maior que zero.")
        except ValueError:
            print("Por favor, digite um número válido.")

    while True:
        try:
            horas_dia = float(input("Digite o tempo médio de uso diário (em horas): "))
            if 0 <= horas_dia <= 24:
                break
            print("O tempo de uso deve estar entre 0 e 24 horas.")
        except ValueError:
            print("Por favor, digite um número válido.")

    consumo_mensal = (potencia * horas_dia * 30) / 1000
    tarifa_kwh = 0.75
    custo_estimado = consumo_mensal * tarifa_kwh

    print("\n" + "-" * 45)
    print(f"Aparelho: {nome_aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
    print(f"Custo estimado (R$ 0,75/kWh): R$ {custo_estimado:.2f}/mês")
    print("-" * 45)

if __name__ == "__main__":
    calcular_consumo()