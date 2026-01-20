with open("dados.txt", "r") as arquivo:
    print("Representação original da linha:")
    for linha in arquivo:
        print(repr(linha))



with open("dados.txt", "r") as arquivo2:
    print("Representação da linha após strip:")
    for linha in arquivo2:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
