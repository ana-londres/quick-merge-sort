# rodar com: python merge.py
import timeit

# Função para o MergeSort
def merge_sort(arr):
    # Verificar se o array tem mais de um elemento (base do caso recursivo)
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontrar o meio do array para dividir em 2 partes
        left_half = arr[:mid]  # Dividir o array em duas metades - esquerda e direita
        right_half = arr[mid:]

        # Chama recursivamente para ordenar cada metade
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializa 3 índices: i- esquerda / j- direite / k- original (preenche com os elementos ordenados)
        i = j = k = 0

        # Copiar dados temporariamente nas duas metades para o array original
        # Enquanto houver elementos em ambas as metades:
        while i < len(left_half) and j < len(right_half):
            # Comparar os elementos das duas metades e adicionar o menor ao array original
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i] # coloca o menor elemento na esquerda
                i += 1 # avança o índice da esquerda
            else:
                arr[k] = right_half[j] # coloca o menor elemento na direita
                j += 1 # avança o índice da direita

            k += 1 # avança o índice do array original

        # Verificar se algum elemento foi deixado na metade esquerda
        # se sim, adicionar ao array original
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Verificar se algum elemento foi deixado na metade direita
        # se sim, adicionar ao array original
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Função para executar o Merge, medir o tempo de execução e salvar em um arquivo .txt
def merge(arquivo_escolhido):
    try:
        # Tenta abrir o arquivo com o nome fornecido e ler os dados (um número por linha)
        with open(arquivo_escolhido, 'r') as arquivo:
            # strip() serve para remover espaços em branco no início e no final da string linha
            # cada linha limpa é convertida para inteiro e adicionada ao array, armazenando-os em uma lista
            array = [int(linha.strip()) for linha in arquivo]
    except FileNotFoundError:
        print(f"Arquivo {arquivo_escolhido} não foi encontrado. Verifique novamente o nome do arquivo.")
        return

    # Marcar o tempo de início
    tempo_inicio = timeit.default_timer()

    # Executar o MergeSort
    merge_sort(array)

    # Marcar o tempo de finalização
    tempo_fim = timeit.default_timer()

    # Calcular o tempo total de execução
    tempo_total = tempo_fim - tempo_inicio

    # Imprimir o array ordenado
    print(f"Array ordenado: {array}\n")

    print(f"Tempo de execução para {arquivo_escolhido}: {tempo_total:.6f} segundos")

    # Salvar o tempo de execução em um arquivo .txt
    with open('merge-time.txt', 'a') as f:
        f.write(f"{arquivo_escolhido}: {tempo_total:.6f} segundos\n")

# Função para selecionar o arquivo de teste e executar o MergeSort
def test():
    # Solicitar ao usuário que insira o nome do arquivo
    arquivo_escolhido = input("Digite o nome do arquivo de teste (por exemplo, 'instancias-num/num.1000.1.in'): ")

    # Executar o MergeSort e salvar o tempo de execução
    merge(arquivo_escolhido)

if __name__ == "__main__":
    test()