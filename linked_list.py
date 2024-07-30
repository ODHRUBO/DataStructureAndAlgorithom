class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        #Empty linked list
        self.head=None
        #number of node in the linked list
        self.n=0 #n=count

    #len function
    def __len__(self):
        return self.n  #number of node in the linked list

   #insert (head) Function
    def insert_head(self,value):
        #new node
        new_node=Node(value)
        #create connection
        new_node.next = self.head
        #reassign head
        self.head = new_node
        #increment n
        self.n=self.n+1

    #traverse function
    def __str__(self):
        curr=self.head
        result=''
        while curr!=None:
            result=result + str(curr.data)+ '->'
            curr=curr.next
        return result[:-2] #slising ->
    
    #append function
    def append (self,value):
        new_node=Node(value)
        if self.head==None:
        # is empty
            self.head=new_node
            self.n=self.n+1
            return

        curr=self.head
        while curr.next !=None:
            curr=curr.next
        #you are the last of the node
        curr.next=new_node
        self.n=self.n=1

    #insert(middle/after) function
    def insert_after(self,after,value):
        new_node=Node(value)
        curr=self.head
        while curr !=None:
            if curr.data==after:
                break
            curr=curr.next

        if curr != None:
            new_node.next=curr.next
            curr.next=new_node
            self.n=self.n+1
        else:
            return 'Item nit found'
        
    #clear function
    def clear(self):
        self.head=None
        self.n=0


    #delet head function
    def delet_head(self):
        if self.head==None:
            #empty
            return 'Empty Linked list'
        self.head=self.head.next
        self.n=self.n - 1

    #delet tail function
    def pop(self):
        if self.head==None:
            return 'Empty list'
        
        curr=self.head
        #is one item exist in list?
        if curr.next==None:
            #existing item is head(so delet the item from head)
            return self.delet_head() 
        
        while curr.next.next!=None:
            curr=curr.next
        #curr ->2nd last node
        curr.next=None
        self.n=self.n - 1

    #removr indrex function
    def remove (self,value):
        if self.head==None:
            return 'Empty linked list'
        
        if self.head.data==value:
            #you want to delet the head node
            return self.delet_head()
        
        curr=self.head
        while curr.next !=None:
            if curr.next.data == value:
                break
            curr=curr.next
        #2 cases:item found or item not found
        if curr.next == None:
            #item not found
            return 'Item not found'
        else:
            curr.next=curr.next.next
            self.n=self.n - 1 

    #search by value  function
    def search(self,item):
        curr=self.head
        pos=0
        while curr != None:
            if curr.data == item:
                return pos
            curr=curr.next
            pos=pos+1
        return 'Not Found'
    
    #search by index function
    def __getitem__(self,index):
        curr=self.head
        pos=0
        while curr!=None:
            if pos==index:
                return curr.data
            curr = curr.next
            pos = pos +1
        
        return 'Index Error'




L=LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
# L.append(5)
# print(L)
# print(len(L))

# L.insert_after(1,20)
# L.insert_after(4,20)
# print(L)
# L.clear()

# L.delet_head()
# L.pop()
# L.pop()
# L.pop()
# L.pop()
# print(L.pop())
# L.remove(1)
# print(L.remove(4))
# L.remove(2)
# L.remove(3)
# print(L.remove(5))
# print(L.search(20))
print(L[3])
print(L[5])
print(L)
