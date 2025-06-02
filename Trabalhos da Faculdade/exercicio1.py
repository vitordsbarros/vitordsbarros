# Mensagem de boas-vindas com meu nome e sobrenome
print("Bem-vindo ao sistema de vendas! Desenvolvido por Vitor S. Barros")

# Entrada de dados do usuário: valor unitário e quantidade
valor_unitario = float(input("Digite o valor unitário do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

# Cálculo do valor total sem desconto
valor_total = valor_unitario * quantidade

# Inicialização da variável de desconto
desconto = 0

# Aplicação das regras de desconto conforme o valor total
if valor_total < 2500:
    desconto = 0  # Sem desconto
elif valor_total >= 2500 and valor_total < 6000:
    desconto = 0.04  # 4%
elif valor_total >= 6000 and valor_total < 10000:
    desconto = 0.07  # 7%
else:
    desconto = 0.11  # 11%

# Cálculo do valor com desconto
valor_com_desconto = valor_total * (1 - desconto)

# Saída de dados no console
print(f"\nResumo do pedido:")
print(f"Valor total sem desconto: R$ {valor_total:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")
