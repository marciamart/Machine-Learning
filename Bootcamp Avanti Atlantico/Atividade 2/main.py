#1. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.
def NUM_IMPAR(list:list):
    list_impar = []
    for number in list:
        if number % 2 != 0:
            list_impar.append(number)
    return list_impar

#2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.
def NUM_PRIMO(list:list):
    list_primo = []
    for number in list:
        for i in range(2, number+1):
            if number % i == 0 and i != number:
                break
            elif i == number:
                list_primo.append(number)
    return list_primo

#3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.
def LIST_DIFERENCA(list_a:list, list_b:list):
    resp = []
    for i in list_a:
        if i not in list_b:
            resp.append(i)
    for i in list_b:
        if i not in list_a:
            resp.append(i)     
    return resp
            
#4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.
def SEG_MAIOR(list:list):
    seg_maior = 0
    maior = 0
    for number in list:
        if number > maior:
            seg_maior = maior
            maior = number
    return seg_maior
        

lista = [2, 3, 4, 8, 9, 13, 17, 293]
listaa = [1, 3, 4, 8, 9, 13, 18, 293]

print(SEG_MAIOR(listaa))