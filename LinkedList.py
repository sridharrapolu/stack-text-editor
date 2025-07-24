class node:
    def __init__(self,data,nextnode=None):
        self.data=data
        self.nextnode=nextnode

class linkedlist:
    def __init__(self):
        self.head=None

#REPLACEING MAX VALUE IN LIST
    def maxvalue(self,data):
        currentnode=self.head
        maxnode=currentnode
        while currentnode is not None:
            if currentnode.data >maxnode.data:
                maxnode=currentnode
            currentnode=currentnode.nextnode
        maxnode.data=data

    def traversall(self):
        currentnode=self.head
        while currentnode is not None:
            print (currentnode.data,"--->",end=" ")
            currentnode=currentnode.nextnode
            # print ("none")
            



         
     
node1=node(3)
node2=node(5)
node3=node(199)
node4=node(3)

node1.nextnode=node2
node2.nextnode=node3
node3.nextnode=node4

a=linkedlist()
a.head=node1
a.maxvalue(122)
a.traversall()
print("max value updated")
