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