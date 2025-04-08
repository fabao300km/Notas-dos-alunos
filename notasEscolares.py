def arredondar_nota(notas):

# Foi criada uma lista vazia para armazenar as notas após o armazenamento
    notas_finais = []
# Se a nota for menor que 38 ela não muda 
    for nota in notas:
        if nota < 38:
            notas_finais.append(nota)  # Notas abaixo de 38 não mudam
        else:
            proximo_multiplo_5 = (nota // 5 + 1) * 5  # Calcula o próximo múltiplo de 5
            if proximo_multiplo_5 - nota < 3:
                notas_finais.append(proximo_multiplo_5)  # Arredonda para o múltiplo de 5
            else:
                notas_finais.append(nota)  # Mantém a nota se a diferença for maior ou igual a 3

    return notas_finais

# Lista de notas escolares
notas = [73, 67, 38, 33]

# Chamando a função e exibindo os resultados
notas_ajustadas = arredondar_nota(notas)
print("Notas ajustadas:", notas_ajustadas)
