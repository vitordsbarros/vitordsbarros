medida = float(input("Digite uma distâcia em metro: ")) # Adiciono um input para fornecer os metros.
print("A distância de {}m corresponde a {:.0f}cm e {:.0f}mm!".format(medida, (medida*100), (medida*1000)))
# Printo um mensagem com os marcadores e formato eles com .format() para organizar e calcular a variável criada no input.
# Coloquei os calculos entre parenteses para não haver conflitos. 