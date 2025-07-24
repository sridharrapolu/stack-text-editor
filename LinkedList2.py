class node:
    def __init__(self,data,nextnode=None):
        self.data=data
        self.nextnode=None

class ll:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("LinkedList is empty")
        else:
            currentnode=self.head
            while currentnode is not None:
                print(currentnode.data ,"-->",end=" ")
                currentnode=currentnode.nextnode

    def insert_at_beging(self,data):
        new_node=node(data)
        new_node.nextnode=self.head
        self.head=new_node

    def insert_at_end(self,data):
        end_node=node(data)
        currentnode=self.head
        while currentnode.nextnode is not None:
            currentnode=currentnode.nextnode
        currentnode.nextnode=end_node

    def insert_at_specific_node(self,position,data):
        specified_node=node(data)
        currentnode=self.head
        for i in range(1,position-1):
            currentnode=currentnode.nextnode
        specified_node.nextnode=currentnode.nextnode
        currentnode.nextnode=specified_node
    
    def  deletion_at_beginng(self):
        currentnode=self.head
        self.head=currentnode.nextnode
        currentnode.nextnode=None


    def deletion_at_end(Self):
        previous_node=Self.head
        currentnode=Self.head.nextnode
        while currentnode.nextnode is not None:
            
            currentnode=currentnode.nextnode
            previous_node=previous_node.nextnode

        previous_node.nextnode=None

    

    def deletion_of_a_specific_node(self,positon):
        previous_node2=self.head
        currrentnode=self.head.nextnode
        for i in range(1,positon-1):
            currrentnode=currrentnode.nextnode
            previous_node2=previous_node2.nextnode

        previous_node2.nextnode=currrentnode.nextnode
        currrentnode.nextnode=None




#creating nodes
node1=node(12)
node2=node(34)
node3=node(90)
node4=node(999)

#linking nodes
node1.nextnode=node2
node2.nextnode=node3
node3.nextnode=node4

linkedlist=ll()
linkedlist.head=node1
linkedlist.insert_at_beging(444)
linkedlist.traversal()
print("   ")
linkedlist.insert_at_end(9994)
linkedlist.traversal()
print("hello")
linkedlist.insert_at_specific_node(4,777)
linkedlist.traversal()
print()
linkedlist.deletion_at_beginng()
linkedlist.traversal()
print("Head deleted")
linkedlist.deletion_at_end()
linkedlist.traversal()
print("last node is deleted")
linkedlist.deletion_of_a_specific_node(4)
linkedlist.traversal()
print("4th positon node has been deleted")