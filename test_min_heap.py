import unittest
from unittest.mock import MagicMock
# from min_heap import MinHeap  # starter storage
from heaps_final.min_heap import MinHeap  # solution storage


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = MinHeap()

    def test_default_heap_insert_works(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        # self.assertEqual(self.storage.storage, [10, 9, 9, 6, 1, 8, 9, 5])
        self.assertEqual(self.heap.storage, [0, 1, 5, 9, 6, 8, 10, 9, 9])

    def test_default_get_min_works(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.assertEqual(self.heap.get_size(), 8)
        self.assertEqual(self.heap.get_min(), 1)

    def test_default_get_min_after_delete(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.heap.delete_min()
        self.assertEqual(self.heap.get_min(), 5)
        self.heap.delete_min()
        self.assertEqual(self.heap.get_min(), 6)
        self.heap.delete_min()
        self.assertEqual(self.heap.get_min(), 8)
        self.heap.delete_min()
        self.assertEqual(self.heap.get_min(), 9)
        self.heap.delete_min()
        self.assertEqual(self.heap.get_min(), 9)
        self.heap.delete_min()
        self.assertEqual(self.heap.get_min(), 9)

    def test_default_delete_elements_in_order(self):
        self.heap.insert(6)
        self.heap.insert(7)
        self.heap.insert(5)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(1)
        self.heap.insert(2)
        self.heap.insert(5)

        descending_order = []

        while self.heap.get_size() > 0:
            descending_order.append(self.heap.delete_min())

        self.assertEqual(descending_order, [1, 2, 5, 5, 6, 7, 8, 10])

    # def test_bubble_up_was_called(self):
    def test_sift_up_was_called(self):
        # self.storage._bubble_up = MagicMock()
        self.heap._sift_up = MagicMock()
        self.heap.insert(5)
        # self.assertTrue(self.storage._bubble_up.called)
        self.assertTrue(self.heap._sift_up.called)

    def test_sift_down_was_called(self):
        self.heap._sift_down = MagicMock()
        self.heap.insert(10)
        self.heap.insert(11)
        self.heap.delete_min()
        self.assertTrue(self.heap._sift_down.called)


if __name__ == '__main__':
    unittest.main()
