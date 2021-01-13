class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = [0]
        self.length = 0
        self.comparator = comparator  # defaults to MaxHeap

    def __len__(self):
        return self.length

    def insert(self, value):
        self.storage.append(value)  # add value to storage
        self.length += 1  # increase length (b/c we're inserting)
        self._sift_up(self.length)  # take the freshly appended element and find its correct position in tree

    def delete_priority(self):
        return_val = self.storage[1]  # copy the priority_element
        self.storage[1] = self.storage[self.length]  # assign root to last element
        self.length -= 1  # reduce length (b/c we're deleting)
        self.storage.pop()  # remove last element
        self._sift_down(1)  # take the root element and find its correct position in the tree
        return return_val

    def get_priority(self):
        return self.storage[1]

    def get_size(self):
        return self.length

    def _sift_up(self, index):
        while index // 2 > 0:
            if self.comparator(self.storage[index], self.storage[index // 2]):
                tmp = self.storage[index // 2]
                self.storage[index // 2] = self.storage[index]
                self.storage[index] = tmp
            index //= 2

    def _find_priority_child_index(self, parent_index):
        if parent_index * 2 + 1 > self.length:  # if right_child does not exist
            return parent_index * 2  # return left_child parent_index

        # if left_child is higher priority than right_child
        elif self.comparator(self.storage[parent_index * 2], self.storage[parent_index * 2 + 1]):
            return parent_index * 2  # return left_child parent_index

        else:  # right_child must exist AND must be higher priority than left_child
            return parent_index * 2 + 1

    def _sift_down(self, index):
        while index * 2 <= self.length:
            priority_child_index = self._find_priority_child_index(index)
            if self.comparator(self.storage[priority_child_index], self.storage[index]):
                temp = self.storage[index]
                self.storage[index] = self.storage[priority_child_index]
                self.storage[priority_child_index] = temp

            index = priority_child_index
