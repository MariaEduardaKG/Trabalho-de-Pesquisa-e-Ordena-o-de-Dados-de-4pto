def pancake_sort(arr):
    # variavel que acompanha o tamanho da parte do array que precisa ser ordenado
    paraordenar = len(arr)
    print("\narray inicial: ", array)
    print("\nfalta ordenar ", paraordenar, " números \n")
    while paraordenar > 1:  # enquanto o indice for maior que 1
        # Encontre o índice do máximo elemento não ordenado
        max_index = arr.index(max(arr[:paraordenar]))
        print("índice do maior elemento: ", max_index)
        # Inverter a sequência do início até o máximo elemento
        arr[:max_index + 1] = reversed(arr[:max_index + 1])
        print("inverte a sequência do inicio até o máximo elemento:", array)
        # Inverter a sequência completa
        arr[:paraordenar] = reversed(arr[:paraordenar])
        print("inverte a sequência:", array)
        paraordenar -= 1  # decrementa o array indicando que o maior elemento encontrado até agora esta na posição correta
        if (paraordenar == 1):
            print("\nnão falta ordenar mais nenhum número!")
        else:
            print("\nfalta ordenar ainda ", paraordenar, " números")
    return arr


array = [7, 2, 5, 1, 9, 3]
ordenar_array = pancake_sort(array)
print("\nordem correta do array: ", ordenar_array)
