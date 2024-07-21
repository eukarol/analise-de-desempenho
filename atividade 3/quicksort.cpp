#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
#include <sys/resource.h>

void quick_sort(std::vector<int>& arr, int left, int right) {
    int i = left, j = right;
    int pivot = arr[(left + right) / 2];
    while (i <= j) {
        while (arr[i] < pivot) i++;
        while (arr[j] > pivot) j--;
        if (i <= j) {
            std::swap(arr[i], arr[j]);
            i++; j--;
        }
    }
    if (left < j) quick_sort(arr, left, j);
    if (i < right) quick_sort(arr, i, right);
}

std::vector<int> read_numbers(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<int> numbers;
    int number;
    while (file >> number) {
        numbers.push_back(number);
    }
    return numbers;
}

void write_numbers(const std::string& filename, const std::vector<int>& arr) {
    std::ofstream file(filename);
    for (int num : arr) {
        file << num << "\n";
    }
}

int main() {
    std::vector<int> numbers = read_numbers("arq.txt");

    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    long initial_memory = usage.ru_maxrss;

    auto start = std::chrono::high_resolution_clock::now();
    
    quick_sort(numbers, 0, numbers.size() - 1);
    
    auto end = std::chrono::high_resolution_clock::now();
    getrusage(RUSAGE_SELF, &usage);
    long final_memory = usage.ru_maxrss;

    write_numbers("arq-saida.txt", numbers);
    
    std::chrono::duration<double, std::milli> elapsed = end - start;
    std::cout << "Tempo de execução: " << elapsed.count() << " ms\n";
    std::cout << "Memória utilizada: " << (final_memory - initial_memory) << " KB\n";

    return 0;
}
