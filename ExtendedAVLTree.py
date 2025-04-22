# Filename: ExtendedAVLTree.py

from AVLTree import AVLTree
from ExtendedAVLNode import ExtendedAVLNode


class ExtendedAVLTree(AVLTree):
    """
    Represents an Extended AVL Tree.
    Manages ExtendedAVLNodes and ensures subtree counts are updated
    during insertion, removal, and rotations.
    """

    def __init__(self):
        """Initializes an empty ExtendedAVLTree."""
        super().__init__()
        self.size = 0

    def make_new_node(self, key):
        """Factory method to create ExtendedAVLNodes."""
        return ExtendedAVLNode(key)

    def insert_key(self, key):
        """Inserts a key while updating subtree counts and rebalancing."""
        inserted_node = None
        insertion_parent = None

        if self.root is None:
            self.root = self.make_new_node(key)
            inserted_node = self.root
        else:
            curr = self.root
            while curr is not None:
                if key < curr.key:
                    if curr.left is None:
                        new_node = self.make_new_node(key)
                        curr.set_left(new_node)
                        inserted_node = new_node
                        insertion_parent = curr
                        curr = None
                    else:
                        curr = curr.left
                elif key > curr.key:
                    if curr.right is None:
                        new_node = self.make_new_node(key)
                        curr.set_right(new_node)
                        inserted_node = new_node
                        insertion_parent = curr
                        curr = None
                    else:
                        curr = curr.right
                else:
                    inserted_node = curr
                    insertion_parent = None
                    curr = None

        # Update counts upward
        if insertion_parent:
            curr = insertion_parent
            while curr:
                curr.update_subtree_key_count()
                curr = curr.get_parent()

            # Rebalance upward
            curr = insertion_parent
            while curr:
                curr = self.rebalance(curr)
                if curr:
                    curr = curr.get_parent()

        self.size = self.get_size()
        return inserted_node

    def remove_key(self, key):
        """Removes a key while updating subtree counts and rebalancing."""
        node_to_remove = self.search(key)
        if node_to_remove is None:
            return False

        rebalance_start_node = node_to_remove.get_parent()
        super(AVLTree, self).remove_node(node_to_remove)

        curr = rebalance_start_node
        while curr:
            curr.update_subtree_key_count()
            curr = curr.get_parent()

        curr = rebalance_start_node
        while curr:
            curr = self.rebalance(curr)
            if curr:
                curr = curr.get_parent()

        self.size = self.get_size() if self.root else 0
        return True

    def rebalance(self, node):
        """Overrides AVLTree rebalance to ensure subtree counts stay correct."""
        if node is None:
            return None

        node.update_height()
        balance = node.get_balance()

        if balance == -2:
            right = node.get_right()
            if right and right.get_balance() == 1:
                self.rotate_right(right)
            return self.rotate_left(node)

        elif balance == 2:
            left = node.get_left()
            if left and left.get_balance() == -1:
                self.rotate_left(left)
            return self.rotate_right(node)

        return node

    def rotate_left(self, node):
        new_root = super().rotate_left(node)
        node.update_subtree_key_count()
        new_root.update_subtree_key_count()
        return new_root

    def rotate_right(self, node):
        new_root = super().rotate_right(node)
        node.update_subtree_key_count()
        new_root.update_subtree_key_count()
        return new_root

    def get_size(self):
        """Returns total number of nodes in tree."""
        if self.root is None:
            return 0
        if isinstance(self.root, ExtendedAVLNode):
            return self.root.get_subtree_key_count()
        raise TypeError("Root must be an ExtendedAVLNode.")

    def get_nth_key(self, n):
        """Returns the nth smallest key using subtree_key_counts (0-based)."""
        if self.root is None or n < 0 or n >= self.get_size():
            raise IndexError("Index out of bounds")
        return self._get_nth_key_helper(self.root, n)

    def _get_nth_key_helper(self, node, n):
        left = node.get_left()
        left_count = left.get_subtree_key_count() if left else 0

        if n == left_count:
            return node.get_key()
        elif n < left_count:
            return self._get_nth_key_helper(left, n)
        else:
            return self._get_nth_key_helper(node.get_right(), n - left_count - 1)
