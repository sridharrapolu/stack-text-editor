class Circular_Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rare=-1

    def enqueue(self,data):
        if (self.rare+1)%self.size==self.front:
            print("circular queue is FULL:")
            
        elif self.front==-1:  #  there is no elements yet 
            self.front=0
            self.rare=0
            self.queue[self.rare]=data
        else:
            self.rare=(self.rare+1)%self.size # insertion while there are elements before
            self.queue[self.rare]=data

    def dequeue(self):
        if self.front==-1:
            print("Circular queue is empty")
        elif self.front==self.rare:  # if there is only one element
            print("Removed element is:",self.queue[self.front])
            self.front=None
            self.front=-1
            self.rare=-1
        else:
            print("Removed element is:",self.queue[self.front]) # regular deletion ie there are elemts in queue before 
            self.queue[self.front]=None
            self.front=(self.front+1)%self.size

    def display(self):
        if self.front==-1:
            print("Circular queue is empty")
        else:
            print("elments are:",end=" ")
            i=self.front
            while True:
            
                print(self.queue[i],end=" ")
                if i==self.rare:
                    break
                i=(i+1)%self.size
        print()





cq=Circular_Queue(5)
cq.enqueue(12)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)  # This should print " is Full"
cq.display()
cq.dequeue()
cq.display()
cq.dequeue()
cq.display()




    