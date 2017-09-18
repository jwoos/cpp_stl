import pytest

import linked_list as ll


class TestLinkedListInitialize:
    def test_initializes(self):
        linked_list = ll.LinkedList()

        assert linked_list.head == None
        assert linked_list.tail == None
        assert linked_list.size == 0

    def test_initializes_with_node(self):
        node = ll.LinkedListNode(data='a')
        linked_list = ll.LinkedList(head=node)

        assert linked_list.head == node
        assert linked_list.tail ==  node
        assert linked_list.size == 1


class TestLinkedListAppend:
    def setup_method(self, method):
        self.linked_list = ll.LinkedList()

    def teardown_method(self, method):
        del self.linked_list

    def test_appends_head(self):
        self.linked_list.append('a')
        assert self.linked_list.head.data == 'a'
        assert self.linked_list.tail.data == 'a'
        assert self.linked_list.size == 1

    def test_appends_body(self):
        self.linked_list.append('a')
        self.linked_list.append('b')

        assert self.linked_list.head.data == 'a'
        assert self.linked_list.tail.data == 'b'
        assert self.linked_list.size == 2


class TestLinkedListPop:
    def setup_method(self, method):
        self.linked_list = ll.LinkedList()

        for i in range(10):
            self.linked_list.append(i)

    def teardown_method(self, method):
        del self.linked_list

    def test_pop(self):
        data = self.linked_list.pop()

        assert data == 9
        assert self.linked_list.size == 9
        assert self.linked_list.head.data == 0
        assert self.linked_list.tail.data == 8

    def test_pop_node(self):
        node = self.linked_list.pop(node=True)

        assert node.data == 9
        assert self.linked_list.size == 9
        assert self.linked_list.head.data == 0
        assert self.linked_list.tail.data == 8
        assert isinstance(node, ll.LinkedListNode)

    def test_pop_all(self):
        for i in range(1, 11):
            data = self.linked_list.pop()
            assert data == (10 - i)

    def test_pop_past_end(self):
        for _ in range(10):
            data = self.linked_list.pop()

        data = self.linked_list.pop()
        assert data == None


class TestLinkedListGet:
    def setup_method(self, method):
        self.linked_list = ll.LinkedList()

        for i in range(10):
            self.linked_list.append(i)

    def teardown_method(self, method):
        del self.linked_list

    def test_get_head(self):
        data = self.linked_list.get(0)

        assert self.linked_list.head.data == data
        assert data == 0

    def test_get_tail(self):
        data = self.linked_list.get(self.linked_list.size - 1)

        assert self.linked_list.tail.data == data
        assert data == 9

    def test_get_body(self):
        data = self.linked_list.get(5)

        assert data == 5

    def test_get_node(self):
        node = self.linked_list.get(1, node=True)

        assert node == self.linked_list.head.next

    @pytest.mark.parametrize('index', [
        (-1),
        (100)
    ])
    def test_get_oob(self, index):
        with pytest.raises(Exception):
            self.linked_list.get(index)


class TestInsert:
    def setup_method(self, method):
        self.linked_list = ll.LinkedList()

    def teardown_method(self, method):
        del self.linked_list

    def test_insert_head(self):
        self.linked_list.insert(0, 0)
        assert self.linked_list.size == 1
        assert self.linked_list.head == self.linked_list.tail
        assert self.linked_list.head.data == 0
        assert self.linked_list.tail.data == 0

    def test_insert_tail(self):
        self.linked_list.insert(0, 0)
        self.linked_list.insert(1, 1)

        assert self.linked_list.size == 2
        assert self.linked_list.head != self.linked_list.tail
        assert self.linked_list.head.data == 0
        assert self.linked_list.tail.data == 1

    def test_insert_body(self):
        self.linked_list.insert(0, 0)
        self.linked_list.insert(1, 1)
        self.linked_list.insert(1, 2)

        assert self.linked_list.size == 3
        assert self.linked_list.head.data == 0
        assert self.linked_list.tail.data == 1
        assert self.linked_list.get(1) == 2

    @pytest.mark.parametrize('index', [
        (-1),
        (100)
    ])
    def test_insert_oob(self, index):
        with pytest.raises(Exception):
            self.linked_list.insert(index, 0)


class TestLinkedListDelete:
    def setup_method(self, method):
        self.linked_list = ll.LinkedList()

        for i in range(10):
            self.linked_list.append(i)

    def teardown_method(self, method):
        del self.linked_list

    def test_delete_head(self):
        self.linked_list.delete(0)

        assert self.linked_list.size == 9
        assert self.linked_list.head.data == 1
        assert self.linked_list.tail.data == 9

    def test_delete_head(self):
        self.linked_list.delete(self.linked_list.size - 1)

        assert self.linked_list.size == 9
        assert self.linked_list.head.data == 0
        assert self.linked_list.tail.data == 8

    def test_delete_body(self):
        self.linked_list.delete(5)

        assert self.linked_list.size == 9
        assert self.linked_list.head.data == 0
        assert self.linked_list.tail.data == 9

    @pytest.mark.parametrize('index', [
        (-1),
        (100)
    ])
    def test_delete_oob(self, index):
        with pytest.raises(Exception):
            self.linked_list.delete(index)
