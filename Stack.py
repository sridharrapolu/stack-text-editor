#Stack is also a linked list but operations are done only through topend
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top_node=None

    def is_empty(self):
         return self.top_node is None
       

    def push(self,data):
        new_node=node(data)
        new_node.next=self.top_node
        self.top_node=new_node
    
    def traversal(self):
        if self.top_node==None:
            print("Stack is empty")
        else:
            top=self.top_node
            while top is not None:
                print(top.data,"")
                top=top.next
    
    def peek(self):
        if self.top_node is None:
            print("stack is empty")
        return print(self.top_node.data)
    

    def pop(self):
        if self.top_node is None:
            print("stack is empty")
            return None
        else:
            poped_value=self.top_node.data
            self.top_node=self.top_node.next
            
            return poped_value
        

def text_editor(text,partten):
    u=Stack()
    r=Stack()

    for i in text:
        u.push(i)
    
    for j in partten:
        if j=='u':
            data=u.pop()
            r.push(data)
        else:
            data=r.pop()
            u.push(data)
    res=" "
    while not u.is_empty():
        res=u.pop() + res
    print(res)

# def reverse_stack(self,string):
#     stack=stack()
#     for i in string:
#         stack.push(i)
#     result=" "
#     while not stack.is_empty():
#         result+=stack.pop()
    
#     print(result)
        

        
#celebrity problelm>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#bracet close problem>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



a=Stack()
a.push(111)
a.push(222)
a.push(333)
a.push(444)
a.push(555)
# a.traversal()
# a.peek()
a.pop()
a.traversal()
# a.reverse_stack("Sridhar")
# print("hai")
text_editor("sridhar","uruu")





       
