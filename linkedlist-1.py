# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
class Node:
    # node definition
    def __init__(self,data):
        self.data=data
        self.next=None
    # # traversal    
    # def traverse(head):
    #     curr=head
    #     while curr:
    #         print(curr.data,"->")
    #         curr=curr.next
    #     print("None")    
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


# ----- Taking input from user -----

values = list(map(int, input("Enter numbers separated by space: ").split()))

head = create_linked_list(values)

print("Linked List:")
print_list(head)        
