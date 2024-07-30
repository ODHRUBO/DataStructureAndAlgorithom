#The/*sky*is//blue(input)
#The Sky is Blue(output)

def change_sent(self):
    temp = self.head
    while temp !=None:
        if temp.data =='*' or temp.data == '/':
            temp.data=' '

            if temp.next.data =='*' or temp.next.data =='/':
                temp.next.next.data=temp.next.next.data.upper()
                temp.next=temp.next.next

        temp = temp.next
        
