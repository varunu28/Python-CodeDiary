class Stack(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

# Tests
a = Stack()
print(a.isEmpty())
a.push(1)
a.push(2)
print(a.peek())
print(a.pop())
print(a.pop())
print(a.isEmpty())