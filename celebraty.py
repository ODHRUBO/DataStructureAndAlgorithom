L=[
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]
def find_the_celeb(L):
    s=Stack()
    for i in range(len(L)):
        s.push(i)
    
    while s.size() >=2:
        i = s.pop()
        j = s.pop()

        if L[i][j]==0:
            #j is not a celebrity
            s.push(i)
        else:
            #is not a celebraty
            s.push(j)
    celeb =  s.pop()
    for i in range(len(L)):
        if i!=celeb:
            if L[i][celeb] == 0 or L[celeb][i]==1:
                print("No one is celebrity")
                return
    print("The celebrity is ",celeb)