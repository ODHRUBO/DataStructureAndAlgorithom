def sum_odd_nodes(self):
    temp=self.head
    counter=0
    result=0

    while temp != None:
        if counter % 2 !=0:
            result=result + temp.data

        counter+=1
        temp=temp.next
    
    print(result)