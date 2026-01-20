frase = "Eu amo comer amoras no café da manhã"

# Resultado obtido utilizando o método count diretamente
print("Contagem direta: {}\n\n".format(frase.count('amo')))

#resultado obtido utilizando a quebra da frase em palavras
contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador =+ 1
print("Contagem correta: {}".format(contador))