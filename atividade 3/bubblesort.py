def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def read_file_to_list(filename):
    arr = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove espaços e converte a linha em inteiro
                arr.append(int(line.strip()))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
    except ValueError:
        print("Erro: O arquivo contém valores não numéricos.")
    return arr

# Nome do arquivo
filename = 'arq.txt'

# Lendo o arquivo e convertendo-o em uma lista
arr = read_file_to_list(filename)

if arr:  # Verifica se a lista não está vazia
    print("Unsorted list is:")
    print(arr)

    bubble_sort(arr)

    print("Sorted list is:")
    print(arr)
else:
    print("A lista está vazia ou houve um erro ao ler o arquivo.")
