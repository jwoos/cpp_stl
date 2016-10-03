#include <vector>

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
