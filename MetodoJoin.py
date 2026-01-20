minha_lista = ['Arroz', 'Feijão', 'Macarrão']

#dando join da string ', ' na minha_lista 
texto1 = ', '.join(minha_lista)
with open('texto.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto1)

#dando join para colocar cada conteúdo da lista minha_lista em uma linha separada
texto2 = '\n'.join(minha_lista)
with open('texto2.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto2)