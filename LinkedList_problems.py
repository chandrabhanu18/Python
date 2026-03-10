class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    curr = head

    for value in values[1:]:
        curr.next = Node(value)
        curr = curr.next

    return head


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")



# Insert at starting
def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node   # new head
# Insert at ending
def insert_at_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = new_node
    return head
# Insert at position
def insert_at_position(head, data, pos):
    new_node = Node(data)

    if pos == 0:
        new_node.next = head
        return new_node

    curr = head
    for _ in range(pos - 1):
        if curr is None:
            return head  # invalid position
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node

    return head
# Delete at beginning
def delete_at_beginning(head):
    if head is None:
        return None
    return head.next

# delete node at end
def delete_at_end(head):
    if head is None or head.next is None:
        return None

    curr = head
    while curr.next.next:
        curr = curr.next

    curr.next = None
    return head

# Reverse a linked list
def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev



# Finding middle of the linked list

def find_middle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow

# Detecting is there any cycle in the list
def cycle_exits(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return "Cycle Exists"
    return "No Cycle"
    

# Merge two sorted linked lists
def merging(l1,l2):
    dummy=Node(0)
    curr=dummy
    while l1 and l2:
        if l1.data<=l2.data:
            curr.next=l1
            l1=l1.next
        else:
            curr.next=l2
            l2=l2.next
        curr=curr.next    
    if l1:
        curr.next=l1
    else:
        curr.next=l2
    return dummy.next    



arr=list(map(int,input().split()))
a=create_linked_list(arr)
print(find_middle(a).data)
    
