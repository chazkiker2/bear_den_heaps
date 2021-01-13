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
    def insert(self, value):
        """This is our client-facing method for inserting a node into the tree.

        Add node into storage, fix self.length, then let _sift_up() do the heavy lifting
        to position the new element correctly.
        """
        pass

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
        pass

    # place the element at given parent_index in its correct position in the tree
    def _sift_down(self, index):
        """Re-balance the tree by shifting the element at given parent_index down the tree until storage order
        property is preserved.

        This method takes the node at the given parent_index and first looks to see if that node has children. If it does,
        check to see if one child is less than the other.
        """
        pass

    # return minimum element in constant time O(1)!
    def get_min(self):
        pass

    # delete the smallest node, then re-balance the tree
    def del_min(self):
        pass

    # given a list, build a new storage accordingly
    def build_heap(self, list_in):
        pass

    # given the parent_index of the parent, find the smaller of that parent's two children
    def _find_min_child_index(self, parent_index):
        pass
