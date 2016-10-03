#include <vector>

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
