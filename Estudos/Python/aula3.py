n1 = int(input("Digite um número: ")) # Aqui eu adiciono um input que irá pedir um número.
n2 = int(input("Digite outro numero: ")) # Aqui vai mais um que pede um outro número.
sum = n1 + n2 # Crio uma variável soma que irá somar as duas variáveis criadas no input.
print("Seus numeros são {} e {}, e a soma deles será {}".format(n1, n2, sum)) # Aqui printo em mensagem as informações fornecidas e o resultado.
# Vale ressaltar que foi preciso criar sum = n1 + n2 pois se eu colocasse eles dessa forma .format(n1 + n2) o resultado sairia por exemplo 17 e não 8.