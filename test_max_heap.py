import unittest
from unittest.mock import MagicMock
# from max_heap import MaxHeap  # starter storage
from heaps_final.max_heap import MaxHeap  # solution storage


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.heap = MaxHeap()

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
        self.assertEqual(self.heap.storage, [0, 10, 9, 9, 6, 1, 8, 9, 5])

    def test_default_get_max_works(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.assertEqual(self.heap.get_size(), 8)
        self.assertEqual(self.heap.get_max(), 10)

    def test_default_get_max_after_delete(self):
        self.heap.insert(6)
        self.heap.insert(8)
        self.heap.insert(10)
        self.heap.insert(9)
        self.heap.insert(1)
        self.heap.insert(9)
        self.heap.insert(9)
        self.heap.insert(5)
        self.heap.delete_max()
        self.assertEqual(self.heap.get_max(), 9)
        self.heap.delete_max()
        self.assertEqual(self.heap.get_max(), 9)
        self.heap.delete_max()
        self.assertEqual(self.heap.get_max(), 9)
        self.heap.delete_max()
        self.assertEqual(self.heap.get_max(), 8)
        self.heap.delete_max()
        self.assertEqual(self.heap.get_max(), 6)

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
            descending_order.append(self.heap.delete_max())

        self.assertEqual(descending_order, [10, 8, 7, 6, 5, 5, 2, 1])

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
        self.heap.delete_max()
        self.assertTrue(self.heap._sift_down.called)

    def test_build_heap(self):
        self.heap.build_heap([2, 3, 5, 6, 9])
        self.assertEqual(self.heap.storage, [0, 9, 6, 5, 2, 3])


if __name__ == '__main__':
    unittest.main()
