class Queue:
    def __init__(self):
        self.item=[]
        self.front=None
        self.rear=None
    def is_empty(self):
        return len(self.item )==0
    def enqueue(self,data):
        self.item.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.item.pop(0)
        else:
            raise IndexError("empty")
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("empty")
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("empty")
    def size(self):
        return len(self.item)

q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print("front= ",q1.get_front(),"rear= ",q1.get_rear())
try:
    q1.dequeue()
    print("total= ",q1.size())
except IndexError as e:
    print(e.args[0])
        