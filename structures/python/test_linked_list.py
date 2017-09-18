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
    pass
