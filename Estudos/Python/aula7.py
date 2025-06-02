# Versão antiga!
pbim = float(input("Digite a nota do primeiro bimestre: ")) # Registra em float o primeiro bimestre.
sbim = float(input("Digite a nota do segundo bimestre: ")) # Registra em float o segundo bimestre.
tbim = float(input("Digite a nota do terceiro bimestre: ")) # Registra em float o terceiro bimestre.
qbim = float(input("Digite a nota do quarto bimestre: ")) # Registra em float o quarto bimestre.

nota = (pbim + sbim + tbim + qbim) / 4 # Crio uma variavel chamada média para fazer o calculo anual do aluno.
print("A média do aluno ao decorrer do ano foi: ") # Aqui aplico dois prints e organizo as informações nos marcadores.
print("{} no primeiro bimestre, {} no segundo bimestre, {} no terceiro bimestre, {} no quarto bimestre, totalizando {:.1f} na média anual!".format(pbim, sbim, tbim, qbim, nota))

# Versão melhorada!
if nota < 6.0: # Aqui adiciono um if que nada mais é: Se(if) a média for abaixo de 6 ele esta reprovado.
    print("Aluno reprovado!") # Retorna a mensagem de reprovação.
elif 6.0 <= nota <= 6.9: # Aqui adiciono um elif que seria um: Se caso(elif) não for abaixo de 6, e for igual a 6 ou até 6.9 ele será provado por média.
    print("Aluno aprovado por média!") # Retorna a mensagem de aprovação por média.
else: # Aqui adiciono um else que seria: Se caso não for(else) abaixo de 6, nem igual ou até 6.9 e for maior, ele será aprovado.
    print("Aluno aprovado!") # Retorna a mensagem de aprovação.

# Eu me empolguei nessa e atualizei!