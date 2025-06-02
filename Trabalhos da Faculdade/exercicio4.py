# Lista para armazenar os livros
livros = []
id_atual = 1  # ID único para cada livro


# Menu principal do sistema
def menu_principal():

    while True:
        print(
            "Bem-vindo à Livraria do Vitor S. Barros"
        )  # Aqui eu dou as boas vindas.

        print("-" * 34)
        print("-" * 34)
        print("-{:^32}-".format("MENU PRINCIPAL"))
        print("-" * 34)
        print("1 - Cadastrar Livro")
        print("2 - Consultar Livro(s)")
        print("3 - Remover Livro")
        print("4 - Encerrar")

        opcao = input(
            "Escolha a opção desejada: "
        )  # Aqui solicita a opção desejada para esse processo.

        if opcao == "1":
            cadastrar_livro()
        elif opcao == "2":
            consultar_livros()
        elif opcao == "3":
            remover_livro()
        elif opcao == "4":
            print(
                "\nEncerrando o sistema..."
            )  # Irá encerrar o sistemacaso escolher a opção 4.
            break
        else:
            print(
                "Opção inválida! Tente novamente."
            )  # Irá invalidar caso escolha uma opção fora das sugeridas.


# Função para cadastrar um livro
def cadastrar_livro():
    global id_atual
    print("\n" + "-" * 36)
    print(
        "-{:^34}-".format("MENU CADASTRAR LIVRO")
    )  # Mais uma vez o menu, so que com outro detalhe.
    print("-" * 36)
    nome = input(
        "Por favor, entre com o NOME do livro: "
    )  # Aqui solicita o nome do livro.
    autor = input(
        "Por favor, entre com o AUTOR do livro: "
    )  # Aqui solicita o nome do autor.
    editora = input(
        "Por favor, entre com a EDITORA do livro: "
    )  # E aqui solicita o nome da editora.
    livro = {"id": id_atual, "nome": nome, "autor": autor, "editora": editora}
    livros.append(
        livro
    )  # Implementei um append, que seria como criar uma pasta em um fichario, nesse caso irá add o livro em um banco de dados de memoria.
    print(f"\nLivro cadastrado com sucesso! ID do livro: {id_atual}")
    id_atual += 1


# Função para consultar livros
def consultar_livros():
    while True:
        print("\n" + "-" * 38)
        print(
            "-{:^36}-".format("MENU CONSULTAR LIVRO")
        )  # Mais uma vez o menu diferente.

        print("-" * 38)
        print("1 - Consultar TODOS os livros")
        print("2 - Consultar por ID")
        print("3 - Consultar por AUTOR")
        print("4 - Retornar ao MENU")

        opcao = input("Escolha a opção desejada: ")  # Aqui solicita uma opção desejada.

        if opcao == "1":
            print("\n-- LISTA DE LIVROS CADASTRADOS --")
            if livros:
                for livro in livros:
                    print("-" * 40)
                    print(f"ID: {livro['id']}")
                    print(f"NOME: {livro['nome']}")
                    print(f"AUTOR: {livro['autor']}")
                    print(f"EDITORA: {livro['editora']}")
            else:
                print("Nenhum livro cadastrado.")
        elif opcao == "2":

            try:
                id_consulta = int(
                    input("Digite o ID do livro: ")
                )  # Aqui pede para solicitar o id do livro, que ao haver varios, irá ser facil de navegar por eles.
                encontrado = False

                for livro in livros:
                    if livro["id"] == id_consulta:
                        print("-" * 40)
                        print(f"ID: {livro['id']}")
                        print(f"NOME: {livro['nome']}")
                        print(f"AUTOR: {livro['autor']}")
                        print(f"EDITORA: {livro['editora']}")
                        encontrado = True

                if not encontrado:
                    print("Livro não encontrado.")  # Foi mal, seu livro nao existe.
            except ValueError:
                print(
                    "ID inválido. Digite apenas números."
                )  # Opa Opa, ora onde vai com esse id desconhecido?
        elif opcao == "3":
            autor_busca = input("Digite o nome do autor: ").lower()
            encontrados = [
                livro for livro in livros if livro["autor"].lower() == autor_busca
            ]
            if encontrados:
                for livro in encontrados:
                    print("-" * 40)
                    print(f"ID: {livro['id']}")
                    print(f"NOME: {livro['nome']}")
                    print(f"AUTOR: {livro['autor']}")
                    print(f"EDITORA: {livro['editora']}")
            else:
                print("Nenhum livro encontrado para este autor.")  # Esse autor existe?
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")


# Função para remover um livro
def remover_livro():
    print("\n" + "-" * 36)
    print("-{:^34}-".format("MENU REMOVER LIVRO"))
    print("-" * 36)
    try:
        id_remover = int(input("Digite o ID do livro a ser removido: "))
        for livro in livros:
            if livro["id"] == id_remover:
                livros.remove(livro)
                print(
                    f"\nLivro com ID {id_remover} removido com sucesso."
                )  # Poxa, eu gostava dele.
                return
        print("Livro não encontrado.")
    except ValueError:
        print("ID inválido. Digite apenas números.")


# Inicia o programa chamando o menu
menu_principal()