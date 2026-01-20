#contando quantos Olá tem no arquivo

with open("dados.txt", "r", encoding="utf-8") as arquivo: 
    texto = arquivo.read()
    contador = texto.lower().count("olá")
    print("Total de Olás = {}".format(contador))