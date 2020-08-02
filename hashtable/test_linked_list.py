from unittest import TestCase, main
from HashTableLinkedList.HashTableLinkedList import HashTableLinkedList
class TestLinkedList(TestCase):
    def setUp(self):
        self.list = HashTableLinkedList()

    """
    test for:
    1. add to front/shift
    2. test remove from head/unshift
    5. test for delete
    """

    def test_shift(self):
        self.assertEqual(len(self.list), 0)

        self.list.shift({"key": "hello", "value": "world"})
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head, {"key": "hello", "value": "world"})
        self.assertEqual(self.list.tail, {"key": "hello", "value": "world"})

        self.list.shift({"key": "foo", "value": "bar"})
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.head, {"key": "foo", "value": "bar"})
        self.assertEqual(self.list.head.next_node, {"key": "hello", "value": "world"})
        self.assertEqual(self.list.tail, {"key": "hello", "value": "world"})

    def test_unshift(self):
        self.list.shift({"key": "hello", "value": "world"})
        self.list.shift({"key": "foo", "value": "bar"})
        self.list.shift({"key": "bar", "value": "baz"})
        self.assertEqual(self.list.head, {"key": "bar", "value": "baz"})
        self.assertEqual(self.list.head.next_node, {"key": "foo", "value": "bar"})
        self.assertEqual(self.list.head.next_node.next_node, {"key": "hello", "value": "world"})

        self.assertEqual(self.list.unshift(), {"key": "bar", "value": "baz"})
        self.assertEqual(self.list.head, {"key": "foo", "value": "bar"})
        self.assertEqual(self.list.head.next_node, {"key": "hello", "value": "world"})
        self.assertEqual(self.list.tail, {"key": "hello", "value": "world"})
        self.assertEqual(len(self.list), 2)

        self.assertEqual(self.list.unshift(), {"key": "foo", "value": "bar"})
        self.assertEqual(len(self.list), 1)
        self.assertEqual(self.list.head, {"key": "hello", "value": "world"})
        self.assertEqual(self.list.tail, {"key": "hello", "value": "world"})

        self.assertEqual(self.list.unshift(), {"key": "hello", "value": "world"})
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)
        self.assertEqual(len(self.list), 0)

    def test_collapse(self):
        self.list.shift({"key": "hello", "value": "world"})
        self.list.shift({"key": "foo", "value": "bar"})
        self.list.shift({"key": "bar", "value": "baz"})
        self.assertEqual(self.list.collapse(), [
            {"key": "bar", "value": "baz"},        
            {"key": "foo", "value": "bar"},
            {"key": "hello", "value": "world"}
        ])
        self.assertIsNone(self.list.head)
        self.assertEqual(len(self.list), 0)

    def test_delete(self):
        self.list.shift({"key": "hello", "value": "world"})
        self.list.shift({"key": "foo", "value": "bar"})
        self.list.shift({"key": "bar", "value": "baz"})
        self.assertEqual(self.list.delete('hello'), {"key": "hello", "value": "world"})
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list.head, {"key": "bar", "value": "baz"})
        self.assertEqual(self.list.tail, {"key": "foo", "value": "bar"})
        self.assertEqual(self.list.delete('bar'), {"key": "bar", "value": "baz"})
        self.assertEqual(self.list.tail, {"key": "foo", "value": "bar"})
        self.assertEqual(self.list.head, {"key": "foo", "value": "bar"})
        self.assertEqual(len(self.list), 1)

    def test_find(self):
        self.list.shift({"key": "hello", "value": "world"})
        self.list.shift({"key": "foo", "value": "bar"})
        self.list.shift({"key": "bar", "value": "baz"})

        self.assertEqual(self.list.find('hello'), {"key": "hello", "value": "world"})
        self.assertEqual(self.list.find('foo'), {"key": "foo", "value": "bar"})
        self.assertEqual(self.list.find('bar'), {"key": "bar", "value": "baz"})
        self.assertEqual(self.list.find('zzz'), None)


if __name__ == '__main__':
    main()
