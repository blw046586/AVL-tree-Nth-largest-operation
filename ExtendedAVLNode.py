# Filename: ExtendedAVLNode.py

from BSTNode import BSTNode


class ExtendedAVLNode(BSTNode):
    """
    Represents a node in an Extended AVL Tree.
    Extends BSTNode with height and subtree key count.
    """

    def __init__(self, key):
        super().__init__(key)
        self.height = 1
        self.subtree_key_count = 1

    def get_height(self):
        """Returns the height of the node."""
        return self.height

    def update_height(self):
        """Updates the height of the node based on its children."""
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        self.height = 1 + max(left_height, right_height)

    def get_balance(self):
        """Calculates the balance factor of the node."""
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height

    def get_subtree_key_count(self):
        """Returns the number of keys in the subtree rooted at this node."""
        return self.subtree_key_count

    def update_subtree_key_count(self):
        left_count = self.left.get_subtree_key_count() if self.left else 0
        right_count = self.right.get_subtree_key_count() if self.right else 0
        self.subtree_key_count = 1 + left_count + right_count

    def set_left(self, new_left):
        """Sets the left child of the node."""
        super().set_left(new_left)
        if new_left is not None:
            new_left.parent = self
        self.update_subtree_key_count()
        self.update_height()

    def set_right(self, new_right):
        """Sets the right child of the node."""
        super().set_right(new_right)
        if new_right is not None:
            new_right.parent = self
        self.update_subtree_key_count()
        self.update_height()

    def __repr__(self):
        return f"ExtendedAVLNode(key={self.key}, height={self.height}, count={self.subtree_key_count})"

