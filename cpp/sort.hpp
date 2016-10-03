#include <utility>
#include <set>
#include <vector>

const int MIN_SIZE = 10;

template <typename T>
void insertionSort(vector<T>& v) {
	for (int i = 1; i < v.size(); i++) {
		T temp = v[i];
		int j = i;

		for (j = i; j > 0 && v[j] < v[j - 1]; j--) {
			v[j] = v[j - 1];
		}

		v[j] = temp;
	}
}

template <typename T>
void merge(vector<T>& v, vector<T>& temp, int leftStart, int leftEnd, int rightEnd) {
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
void mergeSort(vector<T>& v, vector<T>& temp, int start, int end) {
	if (start >= end) {
		return;
	}

	int mid = (start + end) / 2;
	mergeSort(v, temp, start, mid);
	mergeSort(v, temp, mid + 1, end);
}

template <typename T>
void mergeSort(vector<T>& v) {
	vector<T> temp;
	temp.resize(v.size());
	mergeSort(v, temp, 0, v.size() - 1);
}

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

template <typename T>
void selectionSort(vector<T>& v) {
	for (int i = 0; i < v.size(); i++) {
		int low = i;

		for (int j = i + 1; j < v.size(); j++) {
			if (v[j] < v[low]) {
				low = j;
			}
		}

		T temp = v[low];
		v[temp] = v[i];
		v[i] = temp;
	}
}

template <typename T>
void setSort(vector<T>& v) {
	multiset<T> s;
	for (T i : v) {
		s.insert(i);
	}

	v.clear();
	while (!s.empty()) {
		v.push_back(s.pop());
	}
}

template <typename T>
void shellSort(vector<T>& v) {
	for (int gap = v.size() / 2; gap > 0; gap /= 2) {
		for (int i = gap; i < v.size(); i++) {
			T temp = v[i];
			int j;

			for (j = i; j >= gap && temp < v[j - gap]; j-= gap) {
				v[j] = v[j - gap];
			}

			v[j] = temp;
		}
	}
}

