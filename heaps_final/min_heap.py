# noinspection DuplicatedCode
class MinHeap:
    def __init__(self):
        self.storage = [0]
        self.length = 0

    def __len__(self):
        return self.length

    def get_size(self):
        return self.length

    # Easiest and most efficient way to add an element? Append it!
    # Good news about appending: guarantees that we will maintain the complete tree property
    # Bad news: appending will probably violate the storage structure property.
    # Best news: we can write a method that will allow us to regain the storage structure property by
    # comparing the newly added item with its parent! (see `self._sift_up()`)
    def insert(self, item):
        """This is our client-facing method for inserting a node into the tree.

        Add node into storage, fix self.length, then let _sift_up() do the heavy lifting
        to position the new element correctly.
        """

        self.storage.append(item)
        self.length += 1
        self._sift_up(self.length)

    # place the element at given parent_index in its correct position in the tree
    def _sift_up(self, index):
        """This method compares the item at the given parent_index with its parent node and re-adjusts the tree if necessary.

        This method when called during `self.insert()` takes the newly added item and pushes it UP the tree until
        the storage property is successfully preserved in the tree. If the newly added item is very small (in the case
        of a MinHeap), we might have to swap it up several levels — potentially all the way up until it hits the top.
        Here is where our wasted element [0] is important. Notice that we can compute the parent of any node via
        integer division (aka floor division). The parent_index of the current node divided by 2 (then rounded down) is the
        parent_index of the parent node!
        """

        # note: double slash is integer division (or "floor division")
        # divide operands then round result DOWN
        # 5 / 2 = 2.5
        # 5 // 2 = 2
        while index // 2 > 0:  # while the given parent_index has a parent:
            if self.storage[index] < self.storage[index // 2]:  # if current node is less than its parent
                # then swap child with parent
                tmp = self.storage[index // 2]  # make a copy of parent node
                self.storage[index // 2] = self.storage[index]  # assign current node to parent location
                self.storage[index] = tmp  # place the copy of parent node in its child's location (parent_index.e., parent_index)

            index //= 2  # shorthand for `parent_index = parent_index // 2`

    # place the element at given parent_index in its correct position in the tree
    def _sift_down(self, index):
        """Re-balance the tree by shifting the element at given parent_index down the tree until storage order
        property is preserved.

        This method takes the node at the given parent_index and first looks to see if that node has children. If it does,
        check to see if one child is less than the other.
        """

        while (index * 2) <= self.length:  # while element has at least one child
            min_child_idx = self._find_min_child_index(index)  # get the parent_index of the smaller child

            # if current element is larger than its own child, switch child with parent
            if self.storage[index] > self.storage[min_child_idx]:
                # the following three lines swap the element at parent_index with its smallest child
                # since its child is smaller than itself.
                temp = self.storage[index]  # make a temp copy of current element
                self.storage[index] = self.storage[min_child_idx]  # assign the current placement to smaller child
                self.storage[min_child_idx] = temp  # assign temp (current element) to child

            index = min_child_idx

    # return minimum element in constant time O(1)!
    def get_min(self):
        return self.storage[1]

    # delete the smallest node, then re-balance the tree
    def delete_min(self):
        return_val = self.storage[1]  # copy the smallest element
        self.storage[1] = self.storage[self.length]  # set root element to a duplicate of last element
        self.length -= 1  # reduce length (b/c we're deleting an element)
        self.storage.pop()  # remove the original copy of final element (remember we set the root to that element)
        self._sift_down(1)  # take the root element and find its correct position in the tree.
        return return_val  # return the value of the freshly-deleted minimum element

    # given the parent_index of the parent, find the smaller of that parent's two children
    def _find_min_child_index(self, parent_index):
        if parent_index * 2 + 1 > self.length:  # if right child doesn't exist
            return parent_index * 2  # return left child parent_index

        elif self.storage[parent_index * 2] < self.storage[parent_index * 2 + 1]:  # if the left child is smaller than the right child
            return parent_index * 2  # return left child parent_index

        else:  # right child must exist AND must be smaller than left child
            return parent_index * 2 + 1  # return right child parent_index

    # given a list, build a new storage accordingly
    def build_heap(self, list_in):
        idx = len(list_in) // 2
        self.length = len(list_in)
        self.storage = [0] + list_in[:]  # make a copy of list in, set self.storage to that copy but start it with a 0
        while idx > 0:
            self._sift_down(idx)
            idx -= 1


# # Driver code to test BinMinHeap
# mnh = MinHeap()
# mnh.build_heap([9, 5, 6, 2, 3])
# print(mnh.delete_min())
# for i, el in enumerate(mnh.storage):
#     print(f"{i}, {el}")
#
# mnh.insert(4)
# print(f"min {mnh.get_min()}")
# mnh.insert(3)
# for i, el in enumerate(mnh.storage):
#     print(f"{i}, {el}")
#
# print(mnh.delete_min())
# print(mnh.delete_min())
# print(mnh.delete_min())
# print(mnh.delete_min())
