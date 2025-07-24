
class node:
    def __init__(self,data):
        self.data=data
        self.previous_node=None
        self.nextnode=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def forword_traversal(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            currentnode=self.head
            while currentnode is not None:
                print(currentnode.data,"--->",end=" ")
                currentnode=currentnode.nextnode

    def backward_traversal(self):
        if self.head is None:
            print("Doubly LinkedList is empty")
        else:
            currentnode=self.head
            while currentnode.nextnode is not None:
                #print(currentnode.data,end=" ")
                currentnode=currentnode.nextnode
            while currentnode is not None:
                print(currentnode.data,"--->",end=" ")
                currentnode=currentnode.previous_node


    def insertion_at_beging(self,data):
        first_node=node(data)
        currentnode=self.head
        currentnode.previous_node=first_node
        first_node.nextnode=currentnode
        self.head=first_node
    
    
    def insertion_at_end(self,data):
        end_node=node(data)
        currentnode=self.head
        while currentnode.nextnode is not None:
            currentnode=currentnode.nextnode
        currentnode.nextnode=end_node
        end_node.previous_node=currentnode

    def insertion_at_specified_position(self,data,position):
        new_node=node(data)
        currentnode=self.head
        for i in range(1,position-1):
            currentnode=currentnode.nextnode
        new_node.nextnode=currentnode.nextnode
        new_node.previous_node=currentnode
        currentnode.nextnode.previous_node=new_node
        currentnode.nextnode=new_node

    def deletion_at_beging(self):
        currentnode=self.head
        self.head=currentnode.nextnode
        currentnode.nextnode.previous_node=None

    def deletion_at_end(self):
        currentnode=self.head.nextnode
        last_node=self.head
        while currentnode.nextnode  is not None :
            currentnode=currentnode.nextnode
            last_node=last_node.nextnode
        currentnode.prvious_node=None
        last_node.nextnode=None

    def deletion_at_specific_positon(self,postion):
        currentnode=self.head.nextnode
        past_node=self.head
        for i in range(1,postion-1):
            currentnode=currentnode.nextnode
            past_node=past_node.nextnode
        
        past_node.nextnode=currentnode.nextnode
        currentnode.nextnode.previous_node=past_node
        currentnode.nextnode=None
        currentnode.previous_node=None
        
        


        
        


 
            
node1=node(111)
node2=node(222)
node3=node(333)
node4=node(444)
#link  in forward direction
node1.nextnode=node2
node2.nextnode=node3
node3.nextnode=node4
#link in backward direction
node4.previous_node=node3
node3.previous_node=node2
node2.previous_node=node1


dll=DoublyLinkedList()
dll.head=node1


dll.forword_traversal()
print("DLL")

dll.backward_traversal()
print(" ")
dll.insertion_at_beging("000")
dll.forword_traversal()
print("  ")

dll.insertion_at_end(999)
dll.forword_traversal()
print("end node is added")

dll.insertion_at_specified_position(555,5)
dll.forword_traversal()
print("specidied node is added")

dll.deletion_at_beging()
dll.forword_traversal()
print("deleted")

dll.deletion_at_end()
dll.forword_traversal()
print("last node is deleted")

dll.deletion_at_specific_positon(4)
dll.forword_traversal()
print("forward")
dll.backward_traversal()
print("specified node is deleted:555")
