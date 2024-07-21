class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value, position):
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current is not None and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            print("Posição fora do alcance")
        else:
            new_node.next = current.next
            current.next = new_node

    def remove(self, value):
        current = self.head
        prev = None
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        print("Valor não encontrado na lista")

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

def execute_actions(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        initial_list = list(map(int, lines[0].strip().split()))
        actions = lines[1:]

        linked_list = LinkedList()
        for value in reversed(initial_list):
            linked_list.add(value, 0)

        for action in actions:
            parts = action.strip().split()
            if len(parts) == 0:
                continue
            action_type = parts[0]
            if action_type == 'A':
                if len(parts) == 3:
                    value = int(parts[1])
                    position = int(parts[2])
                    linked_list.add(value, position)
            elif action_type == 'R':
                if len(parts) == 2:
                    value = int(parts[1])
                    linked_list.remove(value)
            elif action_type == 'P':
                linked_list.print_list()

if __name__ == "__main__":
    while True:
        print("Digite o nome do arquivo:")
        filename = input()
        try:
            execute_actions(filename)
            break  
        except FileNotFoundError:
            print(f"Erro: O arquivo '{filename}' não foi encontrado. Tente novamente.")
