# Mensagem de boas-vindas com nome e sobrenome
print("Bem-vindo à Loja de Gelados do Vitor S. Barros")
print("--------------------Cardápio--------------------")
print("---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---")
print("   |    P    |   R$ 9.00    |  R$ 11.00 |")
print("   |    M    |   R$ 14.00   |  R$ 16.00 |")
print("   |    G    |   R$ 18.00   |  R$ 20.00 |")
print("----------------------------------------------")

# Inicializa acumulador do valor total
valor_total = 0

# Loop principal para pedidos
while True:
    # Input do sabor
    sabor = input("Entre com o sabor desejado (CP/AC): ").strip().lower()

    # Validação do sabor
    if sabor not in ["cp", "ac"]:
        print("Sabor inválido. Tente novamente")
        continue  # volta ao início do loop

    # Input do tamanho
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").strip().lower()

    # Validação do tamanho
    if tamanho not in ["p", "m", "g"]:
        print("Tamanho inválido. Tente novamente")
        continue  # volta ao início do loop

    # Cálculo do valor com base no sabor e tamanho
    if sabor == "cp":
        if tamanho == "p":
            preco = 9.00
        elif tamanho == "m":
            preco = 14.00
        else:  # G
            preco = 18.00
    elif sabor == "ac":
        if tamanho == "p":
            preco = 11.00
        elif tamanho == "m":
            preco = 16.00
        else:  # G
            preco = 20.00

    # Acumula o valor
    valor_total += preco

    # Mensagem de confirmação do pedido
    sabor_nome = "Cupuaçu" if sabor == "cp" else "Açaí"
    print(f"Você pediu um {sabor_nome} no tamanho {tamanho.upper()}: R$ {preco:.2f}")

    # Pergunta se deseja continuar
    continuar = input("Deseja mais alguma coisa? (S/N): ").strip().lower()
    if continuar == "n":
        break  # sai do loop
    elif continuar != "s":
        print("Entrada inválida. Encerrando pedido por segurança.")
        break

# Saída final do valor a pagar
print(f"\nO valor total a ser pago: R$ {valor_total:.2f}")
