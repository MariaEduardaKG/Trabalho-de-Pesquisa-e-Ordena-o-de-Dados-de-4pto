def bucket_sort(lista, tamanhobucket):
    """
    Ordena uma lista de números inteiros usando o algoritmo Bucket Sort.
    :lista: lista de números inteiros
    :tamanhobucket: tamanho de cada bucket (padrão: 5)
    """
    # determina o valor mínimo e máximo da lista
    min_value = min(lista)
    max_value = max(lista)

    # determina quantos buckets são necessários
    bucket_count = (max_value - min_value) // tamanhobucket + \
        1  # intervalo dos buckets
    print(bucket_count)
    buckets = [[] for _ in range(bucket_count)]  # criando baldes vazios
    print(buckets)

    # distribui os números nos buckets correspondentes
    for num in lista:
        index = (num - min_value) // tamanhobucket
        buckets[index].append(num)
        print(buckets)

    # ordena cada bucket individualmente usando outro algoritmo de ordenação ou o próprio bucket sort de modo recursivo
    for i in range(bucket_count):
        buckets[i] = sorted(buckets[i])
        print(buckets[i])

    # junta todos os buckets em uma única lista ordenada
    return print("Em ordem: ", [num for bucket in buckets for num in bucket])


lista = [11, 9, 21, 8, 17, 19, 13, 1, 24, 12]
print("Fora de ordem: ", lista)
tamanhobucket = 5  # tamanho padrão
bucket_sort(lista, tamanhobucket)
