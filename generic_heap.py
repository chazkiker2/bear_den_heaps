class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = [0]
        self.length = 0
        self.comparator = comparator  # defaults to MaxHeap — lambda x, y: x > y

    def __len__(self):
        return self.length

    def get_size(self):
        return self.length

    def get_priority(self):  # otherwise known as .peek()
        pass

    def delete_priority(self):  # otherwise known as .pop()
        pass

    def insert(self, value):  # otherwise known as .push()
        pass

    def _sift_up(self, index):
        pass

    def _sift_down(self, index):
        pass

    def _find_priority_child_index(self, parent_index):
        pass

    def build_heap(self, list_in):
        pass
