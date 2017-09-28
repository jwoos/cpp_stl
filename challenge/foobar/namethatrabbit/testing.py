import unittest
from solution import answer

class TestSort(unittest.TestCase):
    def test_listlist(self):
        self.assertEqual(answer(['annie', 'bonnie', 'liz'])['list_list'], [[1, 14, 14, 9, 5], [2, 15, 14, 14, 9, 5], [12, 9, 26]])

    def test_sumlist(self):
        self.assertEqual(answer(['annie', 'bonnie', 'liz'])['sum_list'], [43, 59, 47])

    def test_namesumlist(self):
        self.assertEqual(answer(['annie', 'bonnie', 'liz'])['name_sum_list'], [[43, 'annie'], [59, 'bonnie'], [47, 'liz']])

    def test_output(self):
        self.assertEqual(answer(['annie', 'bonnie', 'liz'])['output'], ['bonnie', 'liz', 'annie'])

    def test_samesumsort(self):
        self.assertEqual(answer(['java', 'python', 'ruby', 'c', 'r', 'ab'])['output'], ['python', 'ruby', 'java', 'r', 'c', 'ab'])

if __name__ == '__main__':
    unittest.main()
