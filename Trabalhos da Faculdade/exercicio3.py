# Mensagem de boas-vindas com o seu nome
print("Bem-vindo à Copiadora do Vitor S. Barros")


# Função para escolher o serviço
def escolha_servico():
    while True:
        print("\nEntre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input(">> ").strip().lower()

        if servico == "dig":
            return 1.10
        elif servico == "ico":
            return 1.00
        elif servico == "ipb":
            return 0.40
        elif servico == "fot":
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo de serviço novamente")


# Função para informar o número de páginas com validação de desconto
def num_pagina():
    while True:
        try:
            paginas = int(input("Entre com o número de páginas: "))
            if paginas >= 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.")
            elif paginas >= 2000:
                return paginas * 0.75
            elif paginas >= 200:
                return paginas * 0.80
            elif paginas >= 20:
                return paginas * 0.85
            elif paginas > 0:
                return paginas
            else:
                print("Número inválido de páginas.")
        except:
            print("Valor inválido. Digite um número inteiro.")


# Função para adicionar serviço extra
def servico_extra():
    while True:
        print("\nDeseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        extra = input(">> ").strip()
        if extra == "1":
            return 15.00
        elif extra == "2":
            return 40.00
        elif extra == "0":
            return 0.00
        else:
            print("Opção inválida. Digite novamente.")


# Parte principal do programa
valor_servico = escolha_servico()
paginas_com_desconto = num_pagina()
valor_extra = servico_extra()

# Cálculo total
total = (valor_servico * paginas_com_desconto) + valor_extra

# Resultado final
print(
    f"\nTotal: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {paginas_com_desconto:.0f} + extra: {valor_extra:.2f})"
)
