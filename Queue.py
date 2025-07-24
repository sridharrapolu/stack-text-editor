class Queue:
    def __init__(self):
        self.queue=[]

    def Enqueue(self,data):
        self.queue.append(data)

    def Dequeue(self):
        if len(self.queue)<1:
            print("NONE")
        return self.queue.pop(0)
    
    def peek_first(self):
        print(self.queue[0])
    
    def peek_Last(self):
        print(len(self.queue[(self.queue-1)]))
    
    def display(self):
        print( self.queue)
    
q=Queue()
q.Enqueue(111)
q.Enqueue(222)
q.Enqueue(333)
q.Enqueue(444)
q.Enqueue(555)
q.Enqueue(666)
#q.display()
q.peek_first()
# q.display()
q.peek_Last()



        
