class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

        
M = Node("Mon")
T = Node("Tue")
W = Node("Wed")
TH = Node("TH")
F = Node("Fri")
S = Node("Sat")
Su = Node("Sun")



M.nextval = T
T.nextval = W
W.nextval = TH
TH.nextval = F
F.nextval = S
S.nextval = Su
Su.nextval = None
current =M
while current.dataval :
    print(current.dataval)
    if ( current.nextval ==None) : break
    current = current.nextval
   
