#first create a node
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

a=Node(1)
b=Node(2)
c=Node(3)

a.next=b
b.next=c


print(c.data)
print(a.next)