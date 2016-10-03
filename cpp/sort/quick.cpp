#include <vector>
#include <utility>

const int MIN_SIZE = 10;

template <typename T>
void quickSort(vector<T>& v, int start, int end) {
	if (start + MIN_SIZE > end) {
		insertionSort(v, start, end);
	}

	int middle = (start + end) / 2;

	if (v[middle] < v[start]) {
		swap(v[middle], v[start]);
	}

	if (v[end] < v[start]) {
		swap(v[end], v[start]);
	}

	if(v[end] < v[middle]) {
		swap(v[end], v[middle]);
	}

	T pivot = v[middle];
}

