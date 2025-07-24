# class CircularQueue:
#     def __init__(self, size):
#         self.size = size
#         self.queue = [None] * size  # Fixed-size list
#         self.front = -1
#         self.rear = -1

#     def enqueue(self, data):
#         if (self.rear + 1) % self.size == self.front:
#             print("Queue is Full")
#         elif self.front == -1:  # First insertion
#             self.front = 0
#             self.rear = 0
#             self.queue[self.rear] = data
#         else:
#             self.rear = (self.rear + 1) % self.size
#             self.queue[self.rear] = data

#     def dequeue(self):
#         if self.front == -1:
#             print("Queue is Empty")
#         elif self.front == self.rear:
#             print(f"Removed element: {self.queue[self.front]}")
#             self.queue[self.front] = None
#             self.front = -1
#             self.rear = -1
#         else:
#             print(f"Removed element: {self.queue[self.front]}")
#             self.queue[self.front] = None
#             self.front = (self.front + 1) % self.size

#     def display(self):
#         if self.front == -1:
#             print("Queue is Empty")
#         else:
#             print("Queue elements are:", end=" ")
#             i = self.front
#             while True:
#                 print(self.queue[i], end=" ")
#                 if i == self.rear:
#                     break
#                 i = (i + 1) % self.size
#             print()

# # Example usage
# cq = CircularQueue(5)
# cq.enqueue(10)
# cq.enqueue(20)
# cq.enqueue(30)
# cq.enqueue(40)
# cq.enqueue(50)  # This should print "Queue is Full"
# cq.display()

# cq.dequeue()
# cq.dequeue()
# cq.display()

# cq.enqueue(60)
# cq.enqueue(70)
# cq.display()


int arr=[1,2,3,4,5]
print(arr)

    