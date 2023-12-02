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
  def search(self, data):
    current_node = self.start
    if not self.isEmpty():
      while current_node.next is not None:
        if current_node.item == data:
          return current_node
        current_node = current_node.next
      #following return will only run when item is not found
      return None
  def insert_after(self, prev_node, data = None):
    print(prev_node)
    if prev_node is not None:
      new_node = Node(data, prev_node.next)
      prev_node.next = new_node
  def print_elements(self):
    current_node = self.start
    while current_node is not None:
      print(current_node.item, end=' ')
      current_node = current_node.next
    
new_list = SinglyLinkedList()
new_list.insert_at_start(2)
new_list.insert_at_last(4)
new_list.insert_at_last(8)
new_list.insert_after(new_list.search(4), 6)
new_list.print_elements()
    


