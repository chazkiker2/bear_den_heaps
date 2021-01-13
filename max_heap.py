class MaxHeap:
    def __init__(self):
        self.storage = [0]
        self.length = 0

    def __len__(self):
        return self.length

    def get_size(self):
        return self.length

    def get_max(self):  # otherwise known as .peek()
        pass

    def delete_max(self):  # otherwise known as .pop()
        pass

    def insert(self, value):  # otherwise known as .push()
        pass

    def _sift_up(self, index):
        pass

    def _sift_down(self, index):
        pass

    def _find_max_child_index(self, parent_index):
        pass

    def build_heap(self, list_in):
        pass
