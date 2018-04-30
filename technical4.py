# Question 4
# Find the least common ancestor between two nodes on a binary search tree. 
# The least common ancestor is the farthest node from the root that is an ancestor of both nodes. 
# For example, the root is a common ancestor of all nodes on the tree, 
# but if both nodes are descendents of the root's left child, then that left child might be the 
# lowest common ancestor. You can assume that both nodes are in the tree, 
# and the tree itself adheres to all BST properties.
# The function definition should look like question4(T, r, n1, n2), where T 
# is the tree represented as a matrix, where the index of the list is equal
# to the integer stored in that node and a 1 represents a child node, 
# r is a non-negative integer representing the root, and n1 and n2 are 
# non-negative integers representing the two nodes in no particular order. 
# For example, one test case might be

# question4([[0, 1, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0],
#            [1, 0, 0, 0, 1],
#            [0, 0, 0, 0, 0]],
#           3,
#           1,
#           4)
# and the answer would be 3.

def find_children(n):
    children = []
    node = n
    count = 0
    max = 2
    n_len = len(node)

    for i in xrange(0,n_len):
        while count < max:
            val = n[i]
            if val == 1:
                children.append(i)
                count += 1
            break
    if count == 2:
        return children
    else:
        c_len = len(children)
        for _ in xrange(c_len, max + 1):
            children.append(None)
        return children
        

def find_right(n):
    children = find_children(n)
    # Return the second value
    return children[1]


def find_left(n):
    children = find_children(n)
    # Return the left item
    return children[0]


def question4(T, r, n1, n2):

    if T == None:
        return False

    if type(T) is not list:
        return False

    node_index = r
    node = T[node_index]

    while find_left(node) is not None or find_right(node) is not None:  
        if node_index > n1 and node_index > n2:
            # The current node is larger than each of the other nodes, thus look left
            node = T[node_index]
            node_index = find_left(node)

        elif node_index < n1 and node_index < n2:
            # The current node is smaller than each of the other nodes, thus look right
            node = T[node_index]
            node_index = find_right(node)

        else:
            # The current node is right between the two nodes
            return node_index


def test4():

    print "Q4 Test1 (Edge case) null input: expected outcome False"
    print "Outcome : " + str(question4(None, 1, 2, 3))

    print "Q4 Test2 (Edge case) passing string value: expected outcome False"
    print "Outcome : " + str(question4("hello", 1, 2, 3 ))
    
    M = [[0, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0]]

    root = 3

    node1 = 1
    node2 = 4
    expected = 3
    print "Q4 Test 3: expected outcome True"
    print "Outcome: ", "True" if question4(M, root, node1, node2) == expected else "False"

    # Example tree:
    #        5
    #     /    \
    #    1      2
    #   /  \    /
    #  0    4  3
    
    M = [[0, 0, 0, 0, 0, 0], 
        [1, 0, 0, 0, 1, 0], 
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 0, 0, 0]]

    root = 5
    node1 = 0
    node2 = 4

    expected = 1
    print "Q4 Test 4: expected outcome True"
    print "Outcome: ", "True" if question4(M, root, node1, node2) == expected else "False"
        
test4()
