info = input("Forneça uma informação: ") # Aqui adiciono um input para fornecer as informações dos tipos primitivos.
print("O tipo primitivo dessa informação é:", type(info)) # Aqui ele irá classificar o tipo primitivo da sua informação fornecida.
print("Essa informação possui números:", info.isnumeric()) # Informa se é número.
print("Essa informação é alfabética:", info.isalpha()) # Informa se é alfabético.
print("Essa informação é alfanumérica:", info.isalnum()) # Informa se é alfanumérico.
# Irá notar que o type(info) sempre irá retornar str, isso ocorre porque o input está sendo atribuido como string, por isso introduzi info.is(tipo primitivo desejado) que irá retornar true ou false.