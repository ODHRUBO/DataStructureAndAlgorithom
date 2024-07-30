import ctypes

class Mylist:

    def __init__(self):
        self.size=1
        self.n=0
        #create a c type array =self.size
        self.A=self.__make_array(self.size)

    #len function
    def __len__(self):
        return self.n
    
    #print function
    def __str__(self):
        result =''
        for i in range (self.n):
            result=result + str(self.A[i])+','
        return '[' + result[:-1] + ']'
    
    #index return
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'

    #delet function
    def __delitem__(self,position):
        if 0<= position < self.n:
            for i in range(position,self.n-1):
                self.A[i]=self.A[i+1]

            self.n=self.n-1


    #append function
    def append(self,item):
        if self.n==self.size:
            #resize
            self.__resize(self.size*2)

    #append
        self.A[self.n]=item
        self.n=self.n+1

    #insert function
    def insert(self,position,item):

        if self.n==self.size:
            self.__resize(self.size*2)

        for i in range (self.n,position,-1):
            self.A[i]=self.A[i-1]

        self.A[position]=item
        self.n=self.n+1

    
    #pop function
    def pop(self):
        if self.n==0:
            return 'empty list'
        print (self.A[self.n-1])
        self.n=self.n-1

    #clear function
    def clear(self):
        self.n=0
        self.size=1

    #find function
    def find(self,item):
        for i in range (self.n):
            if self.A[i]==item:
                return i
            return 'ValueError - not in list'
        
    #remove function
    def remove(self,item):
        position=self.find(item)

        if type(position)==int:
            #delet
            self.__delitem__(position)
        else:
            return position

    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size=new_capacity
        #copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        #reassign A
        self.A = B
    
    def __make_array(self,capacity):
        #create a c type array(static,referential) with size capacity
        return (capacity*ctypes.py_object)()
L=Mylist()
# print(len(L))

L.append("hello")
L.append(3.4)
L.append(True)
L.append(100)
L.append(10.12)

# print(len(L))
# print(L)
# print(L[0])
# print(L[4])
# print(L)
# L.pop()
# print(L)
# L.clear()
# print(L)
# print(L.find('hello'))
# L.insert(1,'world')
# print(L)
# del(L[300])
print(L)
L.remove('hello')
print(L)