class Deque(object):
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		temp = self.items[0]
		self.items = self.items[1:]
		return temp


# Test
d =Deque()
print(d.isEmpty())
print(d.size())
d.addFront(1)
d.addRear(2)
print(d.removeFront())
print(d.removeRear())
print(d.isEmpty())
print(d.size())
