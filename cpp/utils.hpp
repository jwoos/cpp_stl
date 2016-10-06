#include <ctime>
#include <iostream>
#include <string>

class Timer {
	public:
		Timer();

		double elapsed() const;

		void reset();

	private:
		double start;
};
