# AVL-tree-Nth-largest-operation
Step 1: Inspect the BSTNode.py and BinarySearchTree.py files
Inspect the BSTNode class declaration for a binary search tree node in BSTNode.py. The BSTNode class has attributes for the key, parent, left child, and right child. Accessor methods exist for each.

Inspect the BinarySearchTree class declaration for a binary search tree in BinarySearchTree.py. The get_nth_key() method is the only unimplemented method that exists.


Step 2: Inspect other files related to the inheritance hierarchy
Classes AVLNode and AVLTree inherit from BSTNode and BinarySearchTree, respectively. Each class is implemented in a read-only file.

Classes ExtendedAVLNode and ExtendedAVLTree are declared, but implementations are incomplete. Both classes must be implemented in this lab.

Six class names are shown in boxes. White boxes representing read-only, completed class implementations. Four white boxes exist: BinarySearchTree, AVLTree, BSTNode, and AVLNode. Yellow boxes represent incomplete class implementations. Two yellow boxes exist: ExtendedAVLTree and ExtendedAVLNode. Arrows between boxes indicate inheritance. ExtendedAVLTree inherits from AVLTree, AVLTree inherits from BinarySearchTree, ExtendedAVLNode inherits from AVLNode, and AVLNode inherits from BSTNode.

Step 3: Understand the purpose of the subtree_key_count attribute
The ExtendedAVLNode class inherits from AVLNode and adds one integer attribute, subtree_key_count. Each node's subtree key count is the number of keys in the subtree rooted at that node. Ex:

Sample AVL tree with subtree key counts shown outside each node. Root node has key=20 and a subtreeKeyCount=7. Root's left child has key=10 and subtreeKeyCount=2. Root's right child  has key=42 and subtreeKeyCount=4. Node 10's right child has key=19 and subtreeKeyCount=1. Node 42's left child has key=30 and subtreeKeyCount=1. Node 42's right has key=55 and subtreeKeyCount=2. Node 55's right child has key=77 and subtreeKeyCount=1.

ExtendedAVLNode's __init__() and get_subtree_key_count() methods are already implemented and should not be changed. Additional methods are needed to ensure that subtree_key_count remains accurate.


Step 4: Implement ExtendedAVLTree and ExtendedAVLNode
Each node in an ExtendedAVLTree must have a correct subtree_key_count after an insertion or removal operation. Determine which methods in AVLTree and AVLNode must be overridden in ExtendedAVLTree and ExtendedAVLNode to keep each node's subtree_key_count correct. New methods can be added along with overridden methods, if desired.

Hint: Consider an update_subtree_key_count() method for the ExtendedAVLNode class. The method requires each child node's subtree_key_count to be correct, and updates the node's subtree_key_count appropriately. Overridden methods in both ExtendedAVLNode and ExtendedAVLTree can call a node's update_subtree_key_count() method as needed.

Once determinations are made, complete the implementation of both the ExtendedAVLTree and ExtendedAVLNode classes. Do not implement ExtendedAVLTree's get_nth_key() in this step. get_nth_key() requires correct subtree counts at each node.


Step 5: Run tests
TreeTestCommand is a base class defined in TreeCommands.py. A TreeTestCommand object is an executable command that operates on a binary search tree. Classes inheriting from TreeTestCommand are also declared in TreeCommands.py:

TreeInsertCommand inserts keys into the tree
TreeRemoveCommand removes keys from the tree
TreeVerifyKeysCommand verifies the tree's keys using an inorder traversal
TreeVerifySubtreeCountsCommand verifies that each node in the tree has the expected subtree key count
TreeGetNthCommand verifies that get_nth_key() returns an expected value
Code in main.py contains three automated test cases. Each test executes a vector of TreeTestCommand objects in sequence. The third test includes TreeGetNthCommands and will not pass until the completion of Step 6. The first two tests should pass after completion of step 4.

Before proceeding to Step 6, verify that the first two tests in main.py pass. Then submit code and ensure that the first two unit tests pass.


Step 6: Implement ExtendedAVLTree's get_nth_key() method
get_nth_key() must return the tree's nth-largest key. The parameter n starts at 0 for the smallest key in the tree. Ex: Suppose a tree has keys: 10, 19, 20, 30, 42, 55, 77. Then get_nth_key(0) returns 10, get_nth_key(1) returns 19, ..., get_nth_key(5) returns 55, and get_nth_key(6) returns 77.

Implement an algorithm that uses the subtree key counts so that get_nth_key() operates in worst case O(log N) time.
