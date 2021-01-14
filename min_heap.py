# noinspection DuplicatedCode
class MinHeap:
    def __init__(self):
        self.storage = [0]
        self.length = 0

    def __len__(self):
        return self.length

    def get_size(self):
        return self.length

    # return minimum element in constant time O(1)!
    def get_min(self):
        pass

    # delete the smallest node
    # this method should do the simple parts of deleting the smallest node
    # then call _sift_down() to do the heavy lifting of ordering the tree
    def delete_min(self):
        pass

    # add a node to the tree!
    # this method should do the simple parts of adding a node
    # then call _sift_up() to do the heavy lifting of tree-ordering
    def insert(self, value):
        pass

    # --------------------------------------------------------------------
    # Notes regarding _sift_up()
    # --------------------------------------------------------------------
    # This method compares the item at the given index with its parent node and re-adjusts the tree if necessary.
    #
    # This method when called during `self.insert()` takes the newly added item and pushes it UP the tree until
    # the heap order property is successfully preserved in the tree.
    # If the newly added item is very small (in the case of a MinHeap), we might have to swap it up several levels:
    # potentially all the way up until it hits the top.
    #
    # Here is where our wasted element [0] is important. Notice that we can compute the parent of any node via
    # integer division (aka floor division). The index of the current node divided by 2 (then rounded down) is the
    # index of the parent node!
    #
    # (<index of child_node>) // 2 = <index of parent_node>
    # --------------------------------------------------------------------

    # place the node at given index into the correct position in the tree
    # sift up pushes one specific node UP through the tree until it is in the correct place
    def _sift_up(self, index):
        pass

    # --------------------------------------------------------------------
    # Notes regarding _sift_down()
    # --------------------------------------------------------------------
    # Re-balance the tree by shifting the element at given index down the tree until storage order
    # property is preserved.
    #
    # This method takes the node at the given index and first looks to see if that node has children. If it does,
    # we'll call our utility _find_min_child_index() function to find which child to examine.
    # After retrieving the proper child to compare, we'll look to see if the child is SMALLER
    # than the parent. If so, we want to push the parent down the tree (because in a min-heap, SMALLER nodes are
    # placed in higher levels). To achieve this: we'll swap the parent and child.
    # --------------------------------------------------------------------

    # place the node at given index into the correct position in the tree
    # sift down pushes one specific node DOWN through the tree until it is in the correct place
    def _sift_down(self, index):
        pass

    # utility function that will be used as a helper in _sift_up() and _sift_down()
    # given a parent index, return the location of that parent's smaller child node
    def _find_min_child_index(self, parent_index):
        pass

    # ----------------------------------------
    # Stretch
    # ----------------------------------------

    # given a list of elements, create a proper heap according to our heap order property (comparator)
    # for the sake of simplicity, we will only implement a full over-write.
    # this will be a CREATE HEAP method that replaces our existing storage entirely.
    def build_heap(self, list_in):
        pass
