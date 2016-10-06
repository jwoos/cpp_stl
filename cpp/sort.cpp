#include <set>
#include <vector>
#include <utility>

// insertion sort
template <typename T>
void insertionSort(std::vector<T>& v) {
	for (int i = 1; i < v.size(); i++) {
		T temp = v[i];
		int j = i;

		for (; j > 0 && v[j] < v[j - 1]; j--) {
			v[j] = v[j - 1];
		}

		v[j] = temp;
	}
}

// insertion sort for range
template <typename T>
void insertionSort(std::vector<T>& v, int start, int end) {
	for (int i = start + 1; i <= end; i++) {
		T temp = v[i];
		int j = i;

		for (; j > start && v[j] < v[j - 1]; j--) {
			v[j] = v[j - 1];
		}

		v[j] = temp;
	}
}

template <typename T>
void merge(std::vector<T>& v, std::vector<T>& temp, int leftStart, int leftEnd, int rightEnd) {
	int rightStart = leftEnd + 1;
	int tempStart = leftStart;
	int tempPosition = leftStart;

	while (leftStart <= leftEnd && rightStart <= rightEnd) {
		if (v[leftStart] < v[rightStart]) {
			temp[tempPosition++] = v[leftStart++];
		} else {
			temp[tempPosition++] = v[rightStart++];
		}
	}

	while (leftStart <= leftEnd) {
		temp[tempPosition++] = v[leftStart++];
	}

	while (rightStart <= rightEnd) {
		temp[tempPosition++] = v[rightStart++];
	}

	for (; tempStart <= rightEnd; tempStart++) {
		v[tempStart] = temp[tempStart];
	}
}

template <typename T>
void mergeSort(std::vector<T>& v, std::vector<T>& temp, int start, int end) {
	if (start >= end) {
		return;
	}

	int mid = (start + end) / 2;
	mergeSort(v, temp, start, mid);
	mergeSort(v, temp, mid + 1, end);

	merge(v, temp, start, mid, end);
}

template <typename T>
void mergeSort(std::vector<T>& v) {
	std::vector<T> temp;
	temp.resize(v.size());

	mergeSort(v, temp, 0, v.size() - 1);
}

const int MIN_SIZE = 10;

template <typename T>
void quickSort(std::vector<T>& v, int start, int end) {
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

	swap(v[middle], v[end - 1]);

	int i = start;
	int j = end - 1;

	while (true) {
		while (v[++i] < pivot) {}

		while (pivot < v[--j]) {}

		if (i < j) {
			swap(v[i], v[j]);
		} else {
			break;
		}
	}

	swap(v[i], v[end - 1]);

	quickSort(v, start, i - 1);
	quickSort(v, i + 1, end);
}

template <typename T>
void quickSort(std::vector<T>& v) {
	quickSort(v, 0, v.size() - 1);
}

// selection sort
template <typename T>
void selectionSort(std::vector<T>& v) {
	for (int i = 0; i < v.size(); i++) {
		int low = i;

		for (int j = i + 1; j < v.size(); j++) {
			if (v[j] < v[low]) {
				low = j;
			}
		}

		T temp = v[low];
		v[low] = v[i];
		v[i] = temp;
	}
}

// set sort
template <typename T>
void setSort(std::vector<T>& v) {
	std::multiset<T> s;
	for (T i : v) {
		s.insert(i);
	}
	v.clear();

	for (typename std::multiset<T>::iterator it = s.begin(); it != s.end(); it++) {
		v.push_back(*it);
	}
	s.clear();
}

// shell sort
template <typename T>
void shellSort(std::vector<T>& v) {
	for (int gap = v.size() / 2; gap > 0; gap /= 2) {
		for (int i = gap; i < v.size(); i++) {
			T temp = v[i];
			int j = i;

			for (; j >= gap && temp < v[j - gap]; j-= gap) {
				v[j] = v[j - gap];
			}

			v[j] = temp;
		}
	}
}

