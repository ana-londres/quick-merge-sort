import time  # Importa o módulo time para medir o tempo de execução

# Função para ordenar a lista usando o QuickSort com Mediana de Três
def ordena(lista):
    tamanho_da_lista = len(lista)
    if tamanho_da_lista > 0:
        quick(lista, 0, tamanho_da_lista - 1)

# Função principal do QuickSort
def quick(lista, inicio, fim):
    if inicio >= fim:  # Condição de parada
        return
    
    # Usa a mediana de três para escolher o pivô
    pivo = mediana_de_tres(lista, inicio, fim)
    
    # Particiona a lista em torno do pivô e retorna a posição final do pivô
    anterior = inicio + 1
    posterior = fim

    while anterior <= posterior:
        while anterior <= posterior and lista[anterior] <= pivo:
            anterior += 1
        while anterior <= posterior and lista[posterior] > pivo:
            posterior -= 1
        if anterior < posterior:
            lista[anterior], lista[posterior] = lista[posterior], lista[anterior]

    # Coloca o pivô na posição correta
    lista[inicio], lista[posterior] = lista[posterior], lista[inicio]

    # Chama recursivamente para as duas partes da lista
    quick(lista, inicio, posterior - 1)
    quick(lista, posterior + 1, fim)

# Função para calcular a Mediana de Três
def mediana_de_tres(lista, inicio, fim):
    meio = (inicio + fim) // 2

    # Pega os três valores (início, meio e fim)
    if lista[inicio] > lista[meio]:
        lista[inicio], lista[meio] = lista[meio], lista[inicio]
    if lista[inicio] > lista[fim]:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
    if lista[meio] > lista[fim]:
        lista[meio], lista[fim] = lista[fim], lista[meio]

    # O valor mediano será o pivô
    lista[inicio], lista[meio] = lista[meio], lista[inicio]
    return lista[inicio]  # Retorna o valor do pivô (mediana de três)

# Função que executa o quickSort e mede o tempo de execução
def quickSort(arquivo_escolhido):
    try:
        # Tenta abrir o arquivo com o nome fornecido e ler os dados (um número por linha)
        with open(arquivo_escolhido, 'r') as arquivo:
            # strip() remove espaços em branco no início e no final da string linha
            # Cada linha limpa é convertida para inteiro e adicionada ao array, armazenando-os em uma lista
            array = [int(linha.strip()) for linha in arquivo]
    except FileNotFoundError:
        print(f"Arquivo {arquivo_escolhido} não foi encontrado. Verifique o nome do arquivo.")
        return

    # Marca o tempo de início
    tempo_inicio = time.perf_counter()

    # Executa o quickSort
    quick(array, 0, len(array) - 1)

    # Marca o tempo de finalização
    tempo_fim = time.perf_counter()

    # Calcula o tempo total de execução
    tempo_total = tempo_fim - tempo_inicio

    # Imprime o array ordenado (opcional)
    print(f"Array ordenado: {array}\n")

    print(f"Tempo de execução para {arquivo_escolhido}: {tempo_total:.6f} segundos")

    # Salva o tempo de execução em um arquivo .txt
    with open('quick-time.txt', 'a') as f:
        f.write(f"{arquivo_escolhido}: {tempo_total:.6f} segundos\n")

# Função para selecionar o arquivo de teste e executar o quickSort
def test():
    # Solicita ao usuário que insira o nome do arquivo
    arquivo_escolhido = input("Digite o nome do arquivo de teste (por exemplo, 'instancias-num/num.1000.1.in'): ")

    # Executa o quick Sort
    quickSort(arquivo_escolhido)

if __name__ == "__main__":
    test()