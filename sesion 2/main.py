import numpy as np

class Node:
    def __init__(self, data = None):
        self.data = data
        self.link = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_from_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.link:
                current = current.link
            current.link = new_node
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " ->")
            current = current.link
        print("None")

    def add_from_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node



arr = LinkedList()
arr.add_from_end(10)
arr.add_from_end(3)
arr.add_from_start(0)
arr.add_from_end(6)
arr.print_list()


