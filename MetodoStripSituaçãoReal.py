
#contando total de linhas do arquivo sem ignorar as linhas em branco
with open("dados.txt", "r") as arquivo:
    print("Total de linhas no arquivo")
    contador = 0
    for linha in arquivo:
        if linha:
            contador += 1
    print("Total = {}\n\n".format(contador))


#contando total de linhas do arquivo ignorando as linhas em branco
with open("dados.txt", "r") as arquivo2:
    print("Total Real de linhas do arquivo")
    contador2 = 0
    for linha in arquivo2:
        if linha.strip():
            contador2 += 1
    print("Total real = {}".format(contador2))