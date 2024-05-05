class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0  #tributo para controlar o tamanho da lista

    def adicionar(self, valor, posicao):
        novo_no = No(valor)
        if posicao < 0 or posicao > self.tamanho:  #p ver se a posição é válida
            print("Posição inválida.")
            return

        if posicao == 0:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            for _ in range(posicao - 1):
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1  #incrementa o tamanho da lista após adicionar o novo nó

    def remover(self, valor):
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1  #decrementando o tamanho da lista dps de remover o nó
                return
            anterior = atual
            atual = atual.proximo

    def imprimir_lista(self):
        atual = self.cabeca
        while atual is not None:
            print(atual.valor, end=' ')
            atual = atual.proximo
        print()

def main():
    nome_arquivo = input("Digite o nome do arquivo: ")
    with open(nome_arquivo, 'r') as arquivo:
        lista_inicial = list(map(int, arquivo.readline().split()))
        num_acoes = int(arquivo.readline())
        lista_encadeada = ListaEncadeada()
        for posicao, valor in enumerate(lista_inicial):  #usei enumerate p obter a posição
            lista_encadeada.adicionar(valor, posicao)

        for _ in range(num_acoes):
            acao, *args = arquivo.readline().split()
            if acao == 'A':
                valor, posicao = map(int, args)
                lista_encadeada.adicionar(valor, posicao)
            elif acao == 'R':
                valor, = map(int, args)
                lista_encadeada.remover(valor)
            elif acao == 'P':
                lista_encadeada.imprimir_lista()

if __name__ == "__main__":
    main()

