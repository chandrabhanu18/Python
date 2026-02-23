class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def linked_list_creation(values):
    if not values:
        return None
    head=Node(values[0])
    curr=head
    for i in values[1:]:
        curr.next=Node(i)
        curr=curr.next
    return head
def print_ll(head):
    curr=head
    while curr:
        print(curr.data,end="->")
        curr=curr.next
    print("None")
values=list(map(int,input("Enter the elements : ").split()))
result_LL=linked_list_creation(values)
print("Linked List : ")
print_ll(result_LL)
        
        
