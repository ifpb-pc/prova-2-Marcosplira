def q1(pessoas = {"Joao": 25, "Maria": 10}):
pessoas = {
    "Leonardo": 30,
    "Mariana": 15,
    "Gustavo": 29,
    "Bianca": 32,
    "Vinícius": 18,
    "Amanda": 26,
    "Henrique": 11,
    "Camila": 27,
    "Felipe": 33,
    "Juliana": 30,
}

def maior_de_18(pessoas):
    lista = []
    for nome, idade in pessoas.items():
        if idade >= 18:
            lista.append(nome)
    return sorted(lista)

print(maior_de_18(pessoas))

def q2(lista1 = [1, 3, 5], lista2 = [2, 4, 6, 8, 10]):
    
lista1 = [1, 3, 5]
lista2 = [2, 4, 6, 8, 10]
lista3 = []
lista4 = [2, 4, 6]
lista5 = []

def intercala(lista1, lista2):
    lista3 = lista1 + lista2
    return sorted(lista3)
print(intercala(lista1, lista2))
print(intercala(lista3, lista4))
print(intercala(lista5, lista4))
print(intercala(lista5, lista5))
print(intercala(lista4, lista5))


def q3(valores = None):
def ler_valores():
    valores = []
    while True:
        valor = int(input("Digite um valor numérico (0 para sair): "))
        if valor == 0:
            break
        valores.append(valor)
    return valores

def processa_lista(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            if len(pares) == 5:
                pares.pop(0)
            pares.append(num)
        else:
            if len(impares) == 5:
                impares.pop(0)
            impares.append(num)
    return pares, impares

valores = ler_valores()
pares, impares = processa_lista(valores)
print("Lista de Pares:", pares)
print("Lista de Ímpares:", impares)


def q4(valores = None):
    #valores = ler_valores()
    # lista_ambrosina = organizar_alturas(valores)
    # return formatar_alturas(lista_ambrosina)






def main():
    pass

if __name__ == "__main__":
    main()


