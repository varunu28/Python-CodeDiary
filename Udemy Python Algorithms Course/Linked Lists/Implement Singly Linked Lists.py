class SinglyLinkedListNode(object):
	
	def __init__(self, value):
		self.value = value
		self.nextnode = None

a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)

a.nextnode = b
b.nextnode = c
