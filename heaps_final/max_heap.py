class MaxHeap:
    def __init__(self):
        self.storage = [0]
        self.length = 0

    def __len__(self):
        return self.length

    def get_size(self):
        return self.length

    def get_max(self):
        return self.storage[1]

    def delete_max(self):
        return_val = self.storage[1]
        self.storage[1] = self.storage[self.length]
        self.length -= 1
        self.storage.pop()
        self._sift_down(1)
        return return_val

    def insert(self, value):
        self.storage.append(value)
        self.length += 1
        self._sift_up(self.length)

    def _sift_up(self, index):
        while index // 2 > 0:  # while given parent_index has a parent
            if self.storage[index] > self.storage[index // 2]:  # if current item > parent item
                tmp = self.storage[index // 2]  # temp = parent item value
                self.storage[index // 2] = self.storage[index]  # assign current item value to parent's location
                self.storage[index] = tmp  # assign parent item value to child/current item's location

            index //= 2  # shorthand for `parent_index = parent_index // 2`

    def _sift_down(self, index):
        while (index * 2) <= self.length:  # while child position exists
            max_child_idx = self._find_max_child_index(index)  # get parent_index of larger child

            # if current item is smaller than item's largest child
            if self.storage[index] < self.storage[max_child_idx]:
                tmp = self.storage[index]  # tmp = current_node
                self.storage[index] = self.storage[max_child_idx]  # set largest_child to current_location
                self.storage[max_child_idx] = tmp  # set current_node to largest_child's location

            index = max_child_idx  # new parent_index = the parent_index of larger child... now repeat

    def _find_max_child_index(self, parent_index):
        if parent_index * 2 + 1 > self.length:  # if parent_index greater than length, right child does not exist
            return parent_index * 2  # return left_child parent_index

        elif self.storage[parent_index * 2] > self.storage[parent_index * 2 + 1]:  # if left_child > right_child
            return parent_index * 2  # return left_child parent_index

        else:  # right_child must exist and must be greater than left_child
            return parent_index * 2 + 1

    def build_heap(self, list_in):
        idx = (len(list_in) // 2)
        self.length = len(list_in)
        self.storage = [0] + list_in[:]
        while idx > 0:
            self._sift_down(idx)
            idx -= 1


# Driver code to test MaxHeap
# bh = MaxHeap()
# bh.build_heap([9, 5, 6, 2, 3])
# print(bh.delete_max())
# print(f"max={bh.get_max()}")
# bh.insert(8)
# bh.insert(8)
# print(f"max={bh.get_max()}")
#
# print(bh.delete_max())
# print(f"max={bh.get_max()}")
# print(bh.delete_max())
# print(f"max={bh.get_max()}")
# print(bh.delete_max())
# print(bh.delete_max())
