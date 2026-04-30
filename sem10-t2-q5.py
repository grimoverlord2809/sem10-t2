# Lê o valor da compra informado pelo usuário
valor = float(input().strip())

# Calcula e exibe o valor de cada parcela de 1x até 24x
for parcela in range(1, 25):
    prestacao = valor / parcela  # Divisão simples sem juros
    print(f"{parcela}x de R$ {prestacao:.2f}")
