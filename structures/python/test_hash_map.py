from unittest.mock import Mock, patch

import pytest

import hash_map as hm


class TestHashMapInitialize:
    def test_initialize_error_no_size(self):
        with pytest.raises(Exception):
            self.hash_map = hm.HashMap()

    def test_initialize_with_size(self):
        self.hash_map = hm.HashMap(10)

        assert self.hash_map.size == 0
        assert self.hash_map.max_size == 10


class TestHashMapSet:
    def setup_method(self, method):
        self.hash_map = hm.HashMap(10)

    def teardown_method(self, method):
        del self.hash_map

    @patch('hash_map.hash')
    def test_set_empty(self, mocked_hash):
        mocked_hash.return_value = 0

        self.hash_map.set('a', 1)

        hash_node = self.hash_map._store[0].head.data

        assert self.hash_map.size == 1
        assert hash_node.key == 'a'
        assert hash_node.data == 1

    @patch('hash_map.hash')
    def test_set_overwrites(self, mocked_hash):
        mocked_hash.return_value = 0

        self.hash_map.set('a', 1)
        self.hash_map.set('a', 2)

        hash_node = self.hash_map._store[0].head.data

        assert self.hash_map.size == 1
        assert hash_node.key == 'a'
        assert hash_node.data == 2

    @patch('hash_map.hash')
    def test_set_chains(self, mocked_hash):
        mocked_hash.return_value = 0

        self.hash_map.set('a', 0)
        self.hash_map.set('b', 1)
        self.hash_map.set('c', 2)

        chain = self.hash_map._store[0]
        current = chain.head
        for i in range(chain.size):
            assert current.data.data == i
            current = current.next

    @patch('hash_map.hash')
    def test_set_adds(self, mocked_hash):
        mocked_hash.return_value = 0
        self.hash_map.set('a', 0)

        mocked_hash.return_value = 1
        self.hash_map.set('b', 1)

        for i in range(1):
            chain = self.hash_map._store[i]
            current = chain.head
            for j in range(chain.size):
                assert current.data.data == j
                current = current.next

    def test_set_fails_over_size(self):
        for i in range(11):
            result = self.hash_map.set(chr(ord('a') + i), i)
            if i != 10:
                assert result
            else:
                assert not result


class TestHashMapGet:
    @patch('hash_map.hash')
    def setup_method(self, method, mocked_hash):
        self.hash_map = hm.HashMap(20)
        for i in range(10):
            mocked_hash.return_value = i
            self.hash_map.set(chr(ord('a') + i), i)
            self.hash_map.set(chr(ord('a') + 10 + i), i)

    def teardown_method(self, method):
        del self.hash_map

    @patch('hash_map.hash')
    def test_get(self, mocked_hash):
        for i in range(10):
            mocked_hash.return_value = i

            assert self.hash_map.get(chr(ord('a') + i)) == i
            assert self.hash_map.get(chr(ord('a') + 10 + i)) == i

    def test_get_not_found(self):
        data = self.hash_map.get('z')

        assert data is None


class TestHashMapDelete:
    @patch('hash_map.hash')
    def setup_method(self, method, mocked_hash):
        self.hash_map = hm.HashMap(30)
        for i in range(10):
            mocked_hash.return_value = i
            ch = chr(ord('a') + i)
            self.hash_map.set(ch, i)
            self.hash_map.set(ch * 2, i)
            self.hash_map.set(ch * 3, i)

    def teardown_method(self, method):
        del self.hash_map

    @patch('hash_map.hash')
    def test_delete_head(self, mocked_hash):
        self.hash_map.print()
        mocked_hash.return_value = 0
        data = self.hash_map.delete('a')

        assert data == 0
        assert self.hash_map._store[0].size == 0
        assert self.hash_map.size == 29
