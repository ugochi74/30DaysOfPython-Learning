class Node:
    def __init__(self, value):
        # 1. Store the value for the node
        self.value = value
        
        # 2. Instantiate the node without a next value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


# 1. Create a few nodes
node1 = Node(10)
node2 = Node(20)

# 2. Link them together manually to see how it works
node1.next = node2

# 3. Create the empty list
my_list = LinkedList()
my_list.head = node1
my_list.tail = node2

# Print to confirm everything is working!
print(f"Head Node Value: {my_list.head.value}")
print(f"Next Node Value: {my_list.head.next.value}")
print(f"Tail Node Value: {my_list.tail.value}")
