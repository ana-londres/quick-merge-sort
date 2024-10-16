# Linha para execução: python merge.py

import timeit

# Função para a lógica de mesclagem do MergeSort
def merge(arr):
    # verifica se o array tem mais de um elemento (base do caso recursivo)
    if len(arr) > 1:
        mid = len(arr) // 2  # encontra o meio do array para dividir em 2 partes
        left_half = arr[:mid]  # divide o array em duas metades - esquerda e direita
        right_half = arr[mid:]

        # chama recursivamente para ordenar cada metade
        merge(left_half)
        merge(right_half)

        # inicializa 3 índices: i- esquerda / j- direite / k- original (preenche com os elementos ordenados)
        i = j = k = 0

        # copia dados temporariamente nas duas metades para o array original
        # enquanto houver elementos em ambas as metades:
        while i < len(left_half) and j < len(right_half):
            # compara os elementos das duas metades e adicionar o menor ao array original
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i] # coloca o menor elemento na esquerda
                i += 1 # avança o índice da esquerda
            else:
                arr[k] = right_half[j] # coloca o menor elemento na direita
                j += 1 # avança o índice da direita

            k += 1 # avança o índice do array original

        # verifica se algum elemento foi deixado na metade esquerda
        # se sim, adicionar ao array original
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # verifica se algum elemento foi deixado na metade direita
        # se sim, adicionar ao array original
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Função para executar a mesclagem, medir o tempo de execução e salvar em um arquivo .txt
def mergeSort(arquivo_escolhido):
    try:
        # tenta abrir o arquivo com o nome fornecido e ler os dados (um número por linha)
        with open(arquivo_escolhido, 'r') as arquivo:
            # strip() serve para remover espaços em branco no início e no final da string linha
            # cada linha limpa é convertida para inteiro e adicionada ao array, armazenando-os em uma lista
            array = [int(linha.strip()) for linha in arquivo]
    except FileNotFoundError:
        print(f"Arquivo {arquivo_escolhido} não foi encontrado. Verifique novamente o nome do arquivo.")
        return

    # marca o tempo de início
    tempo_inicio = timeit.default_timer()

    # executa o MergeSort
    merge(array)

    # marca o tempo de finalização
    tempo_fim = timeit.default_timer()

    # calcula o tempo total de execução
    tempo_total = tempo_fim - tempo_inicio

    # imprime o array ordenado
    print(f"Array ordenado: {array}\n")

    print(f"Tempo de execução para {arquivo_escolhido}: {tempo_total:.6f} segundos")

    # salva o tempo de execução em um arquivo .txt
    with open('merge-time.txt', 'a') as f:
        f.write(f"{arquivo_escolhido}: {tempo_total:.6f} segundos\n")

# Função para selecionar o arquivo de teste e executar o MergeSort
def test():
    # solicita ao usuário que insira o nome do arquivo
    arquivo_escolhido = input("Digite o nome do arquivo de teste (por exemplo, 'instancias-num/num.1000.1.in'): ")

    # executa o Merge Sort
    mergeSort(arquivo_escolhido)

if __name__ == "__main__":
    test()