# Problem Set 4A
# Name:
# Collaborators:

from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10)))
tree3 = Node(5, Node(3, Node(2), Node(4)), Node(14, Node(12), Node(21, Node(20), Node(26))))

def find_tree_height(tree):
    '''
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    '''
    height = 0
    height_left = 0
    height_right = 0

    right_child = Node.get_right_child(tree)
    left_child = Node.get_left_child(tree)
    if not left_child == None:
        height_left = find_tree_height(left_child) +1
    if not right_child == None:
       height_right = find_tree_height(right_child) +1
    
    if height_left > height_right:
        height = height_left 
    else:
        height = height_right 
    
    return height 

def compare_func(child_value, parent_value):
    if child_value < parent_value:
        return True
    return False
# min heap comparator
#def compare_func(child_value, parent_value):
#    if child_value > parent_value:
#        return True
#    return False   

def is_heap(tree, compare_func):
    '''
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    '''
    right_child = Node.get_right_child(tree)
    left_child = Node.get_left_child(tree)
    value_root = Node.get_value(tree)

    if not left_child == None:
        result = is_heap(left_child, compare_func)
    if not right_child == None:
        result = is_heap(right_child, compare_func)
    
    
    if right_child == None and left_child != None:
        temp = compare_func(Node.get_value(left_child), value_root)
        result = result and temp
    elif left_child == None and right_child != None:
        temp = compare_func(Node.get_value(right_child), value_root)
        result = result and temp
    elif left_child != None and right_child != None:
        temp = compare_func(Node.get_value(right_child), value_root) and compare_func(Node.get_value(left_child), value_root)
        result = result and temp
    else:
        result = True
    return result



if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    #print(find_tree_height(tree1))
    #print(is_heap(tree1, compare_func))
    pass
