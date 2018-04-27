# Question 5
# Find the element in a singly linked list that's m elements from the end. 
# For example, if a linked list has 5 elements, the 3rd element from the end is the 3rd element. 
# The function definition should look like question5(ll, m), where ll is the first node of a linked
# list and m is the "mth number from the end". You should copy/paste the Node class below to
# use as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element


def question5(first, m):

    ll_array = []

    current = first
    while current is not None:
        ll_array.append(current.value)
        current = current.next

    result = ll_array[-m] 

    return result


def test5():
    e1 = Node(1)
    e2 = Node(2)
    e3 = Node(3)
    e4 = Node(4)
    e5 = Node(5)

    ll = LinkedList(e1)

    ll.append(e2)
    ll.append(e3)
    ll.append(e4)
    ll.append(e5)
    
    m = 3

    expected = 3

    print "Case 1 : ", "Pass" if question5(e1,m) == expected else "False"

    ll = None

    e1 = Node(13)
    e2 = Node(12)
    e3 = Node(11)
    e4 = Node(10)
    e5 = Node(9)
    e6 = Node(8)
    e7 = Node(7)
    e8 = Node(6)
    e9 = Node(5)
    e10 = Node(4)
    e11 = Node(3)
    e12 = Node(2)
    e13 = Node(1)

    ll = None
    ll = LinkedList(e1)
    ll.append(e2)
    ll.append(e3)
    ll.append(e4)
    ll.append(e5)
    ll.append(e6)
    ll.append(e7)
    ll.append(e8)
    ll.append(e9)
    ll.append(e10)
    ll.append(e11)
    ll.append(e12)
    ll.append(e13)

    m = 8

    expected = 8

    print "Case 2 : ", "Pass" if question5(e1,m) == expected else "False"

test5()