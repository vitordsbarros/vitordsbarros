num = int(input("Digite um número: ")) # Adiciono um input com int para receber informações de números inteiros.
print("Seu número é {}, o dobro dele é {}, o triplo é {}, e a raiz quarada dele é {:.2f}!".format(num, num*2, num*3, num**(1/2)))
# Aqui adicionei as informações dentro dos marcadores organizadas no .format()... 
# Vale ressaltar que para calcular a raiz quadrada precisa ser numero**(1/2), caso não fizer isso o resultado sairá diferente.
# :.2f serve para o numero não ficar uma bagunça, saindo de 3.266562, para 3.2... (isso é um exemplo!)