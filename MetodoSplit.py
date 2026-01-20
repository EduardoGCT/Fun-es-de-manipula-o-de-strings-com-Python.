#Utilizamos o método split sem argumentos, linha 2, e imprimimos a lista retornada na linha 3. Observe pelo console que cada item da lista é uma palavra da frase.
frase1 = "Eu amo comer amoras no café da manhã"
lista_termos1 = frase1.split()
print(lista_termos1)

#Utilizamos o método split, também, sem argumentos, linha 6, e imprimimos a lista retornada na linha 7. Observe pelo console que, mesmo havendo muitos espaços em 
# branco entre as palavras da frase, a lista contém apenas as palavras, sem nenhum espaço adicional. O Python é esperto o suficiente para detectar vários espaços 
# contínuos e tratá-los como um único separador. 
frase2 = "Amora  abacaxi  abacate  banana"
lista_termos2 = frase2.split()
print(lista_termos2)

#Temos, na linha 9, a última frase: "Carro,moto,avião". Desta vez, utilizamos o método split passando uma vírgula ( , ) como argumento, na linha 10. O resultado é 
# uma lista contendo apenas as palavras, sem o separador, conforme podemos ver pelo console. 
frase3 = "carro,moto,aviao"
lista_termos3 = frase3.split(',')
print(lista_termos3)