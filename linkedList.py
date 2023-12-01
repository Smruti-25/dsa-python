"""Singly linkedList"""

class Node:
  def __init__(self, item = None, next = None):
    self.item = item
    self.next = next

class SinglyLinkedList:
  def __init__(self, start = None):
    self.start = start
  def isEmpty(self):
    return self.start == None
  def insert_at_start(self, data = None):
    new_node = Node(data, self.start)
    self.start = new_node
  def insert_at_last(self, data = None):
    new_node = Node(data, None)
    if not self.isEmpty():
      currentNode = self.start
      while currentNode.next is not None:
        currentNode = currentNode.next
      currentNode.next = new_node
    else:
      self.start = new_node
  def search(self, item = None):


