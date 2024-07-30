class Node:
    def __inti__(self,value):
        self.data=value
        self.next=None

class Stack:
    def __inti__(self):
        self.top=None

    def isempty(self):
        return self.top == None
    
    #push function
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.top
        self.top=new_node 

    #peek function
    def peek(self):
        if(self.isempty()):
            return 'Stack Empty'
        else:
            return self.top.data
        
    #pop function
    def pop(self):

        if(self.isempty()):
            return 'Stack Empty'
        else:
            self.top=self.top.next

    #traversal function
    def traverse(self):
        temp=self.top
        while temp != None:
            print(temp.data)
            temp=temp.next 

s=Stack()
print(s.isempty())

s.push(3)
s.push(4)
s.traverse()
print(s)
print(s.peek())





