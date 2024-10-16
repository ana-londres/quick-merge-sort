import time  # Importa o módulo time para medir o tempo de execução

# Função principal do Quick Sort, responsável pela recursão
def quick(arr, primeiro, ultimo):
    if primeiro < ultimo:  # Verifica se ainda há elementos para ordenar
        # Chama a função de partição para dividir a lista e retorna o ponto de divisão (pivô)
        pivo = partition(arr, primeiro, ultimo)
        
        # Recursivamente aplica o quickSort na sublista à esquerda do pivô
        quick(arr, primeiro, pivo - 1)
        
        # Recursivamente aplica o quickSort na sublista à direita do pivô
        quick(arr, pivo + 1, ultimo)

# Função de partição, que organiza os elementos em torno do pivô
def partition(arr, primeiro, ultimo):
    pivot = arr[primeiro]  # Escolhe o primeiro elemento como o pivô
    leftmark = primeiro + 1  # Define o marcador da esquerda, que começa logo após o pivô
    rightmark = ultimo  # Define o marcador da direita, que começa no final da lista

    while True:  # Laço infinito até que a partição seja concluída
        # Move o marcador da esquerda até encontrar um valor maior que o pivô
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1
        
        # Move o marcador da direita até encontrar um valor menor que o pivô
        while arr[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1

        # Se os marcadores se cruzarem, a partição termina
        if rightmark < leftmark:
            break
        else:
            # Troca os elementos em leftmark e rightmark se ainda não se cruzaram
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    # Coloca o pivô na sua posição correta, trocando com o elemento em rightmark
    arr[ultimo], arr[rightmark] = arr[rightmark], arr[primeiro]
    
    return rightmark  # Retorna a posição final do pivô (splitpoint)

# Função que executa o quickSort e mede o tempo de execução
def quickSort(arquivo_escolhido):
    try:
        # tenta abrir o arquivo com o nome fornecido e ler os dados (um número por linha)
        with open(arquivo_escolhido, 'r') as arquivo:
            # strip() remove espaços em branco no início e no final da string linha
            # cada linha limpa é convertida para inteiro e adicionada ao array, armazenando-os em uma lista
            array = [int(linha.strip()) for linha in arquivo]
    except FileNotFoundError:
        print(f"Arquivo {arquivo_escolhido} não foi encontrado. Verifique o nome do arquivo.")
        return

    # marca o tempo de início
    tempo_inicio = time.perf_counter()

    # executa o quickSort
    quick(array, 0, len(array) - 1)

    # marca o tempo de finalização
    tempo_fim = time.perf_counter()

    # calcula o tempo total de execução
    tempo_total = tempo_fim - tempo_inicio

    # imprime o array ordenado (opcional)
    print(f"Array ordenado: {array}\n")

    print(f"Tempo de execução para {arquivo_escolhido}: {tempo_total:.6f} segundos")

    # salva o tempo de execução em um arquivo .txt
    with open('quick-time.txt', 'a') as f:
        f.write(f"{arquivo_escolhido}: {tempo_total:.6f} segundos\n")

# Função para selecionar o arquivo de teste e executar o quickSort
def test():
    # solicita ao usuário que insira o nome do arquivo
    arquivo_escolhido = input("Digite o nome do arquivo de teste (por exemplo, 'instancias-num/num.1000.1.in'): ")

    # executa o quick Sort
    quickSort(arquivo_escolhido)

if __name__ == "__main__":
    test()
