#include <vector>

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

