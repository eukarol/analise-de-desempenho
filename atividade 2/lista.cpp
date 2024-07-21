#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

class Node {
public:
    int value;
    Node* next;
    Node(int val) : value(val), next(nullptr) {}
};

class LinkedList {
public:
    Node* head;
    LinkedList() : head(nullptr) {}

    void add(int value, int position) {
        Node* new_node = new Node(value);
        if (position == 0) {
            new_node->next = head;
            head = new_node;
            return;
        }
        Node* current = head;
        int count = 0;
        while (current != nullptr && count < position - 1) {
            current = current->next;
            count++;
        }
        if (current == nullptr) {
            std::cout << "Posição fora do alcance" << std::endl;
        } else {
            new_node->next = current->next;
            current->next = new_node;
        }
    }

    void remove(int value) {
        Node* current = head;
        Node* prev = nullptr;
        while (current != nullptr) {
            if (current->value == value) {
                if (prev == nullptr) {
                    head = current->next;
                } else {
                    prev->next = current->next;
                }
                delete current;
                return;
            }
            prev = current;
            current = current->next;
        }
        std::cout << "Valor não encontrado na lista" << std::endl;
    }

    void print_list() const {
        Node* current = head;
        while (current != nullptr) {
            std::cout << current->value << " -> ";
            current = current->next;
        }
        std::cout << "None" << std::endl;
    }
};

void execute_actions(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cout << "Erro: O arquivo '" << filename << "' não foi encontrado. Tente novamente." << std::endl;
        return;
    }

    LinkedList list;
    std::string line;
    std::getline(file, line);
    std::istringstream iss(line);
    int value;
    while (iss >> value) {
        list.add(value, 0);
    }

    while (std::getline(file, line)) {
        char action;
        int value, position;
        std::istringstream action_stream(line);
        if (action_stream >> action >> value >> position) {
            if (action == 'A') {
                list.add(value, position);
            }
        } else if (action_stream >> action >> value) {
            if (action == 'R') {
                list.remove(value);
            }
        } else if (line[0] == 'P') {
            list.print_list();
        }
    }
    file.close();
}

int main() {
    std::string filename;
    while (true) {
        std::cout << "Digite o nome do arquivo:" << std::endl;
        std::cin >> filename;
        execute_actions(filename);
        break;
    }
    return 0;
}
