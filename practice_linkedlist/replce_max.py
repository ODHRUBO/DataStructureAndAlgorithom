
def replace_max(self,value):
    temp=self.head
    max=temp

    while temp !=None:
        if temp.data>max.data:
            max=temp
        temp=temp.next
    max.data=value 
 


