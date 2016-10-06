#include <set>
#include <vector>

template <typename T>
void insertionSort(std::vector<T>& v);

// insertion sort for range
template <typename T>
void insertionSort(std::vector<T>& v, int start, int end);

template <typename T>
void mergeSort(std::vector<T>& v, std::vector<T>& temp, int start, int end);

template <typename T>
void mergeSort(std::vector<T>& v);

template <typename T>
void quickSort(std::vector<T>& v, int start, int end);

template <typename T>
void quickSort(std::vector<T>& v);

template <typename T>
void selectionSort(std::vector<T>& v);

template <typename T>
void setSort(std::vector<T>& v);

template <typename T>
void shellSort(std::vector<T>& v);

#include "sort.cpp"
