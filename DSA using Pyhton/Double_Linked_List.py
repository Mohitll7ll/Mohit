class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        if self.is_empty():
            self.insert_at_start(data)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(temp, data, None)
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, node, data):
        if node is not None:
            n = Node(node, data, node.next)
            if node.next is not None:
                node.next.prev = n
            node.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_item(self, data):
        if self.start is None:
            return
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp == self.start:
                    self.start = temp.next
                break
            temp = temp.next

    def __iter__(self):
        return DLLiterator(self.start)

class DLLiterator:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

mylist = DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(10), 15)
for x in mylist:
    print(x, end=" ")
print()
