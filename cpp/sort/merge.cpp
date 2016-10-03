#include <vector>

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

// O(n*log(n))
template <typename T>
void mergeSort(vector<T>& v) {
	vector<T> temp;
	temp.resize(v.size());
	mergeSort(v, temp, 0, v.size() - 1);
}

