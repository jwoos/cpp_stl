#include <vector>

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

