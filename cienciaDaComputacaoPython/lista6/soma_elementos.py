# Escreva a função soma_elementos que recebe como parâmetro 
# uma lista com números inteiros e devolve um número inteiro 
# correspondente à soma dos elementos da lista recebida.

def soma_elementos(lista):
    aux = 0
    for i in lista:
        aux+=i
    return aux