class Queue2Stacks(object):
    
    def __init__(self):
        # Two Stacks
        self.instack = []
        self.outstack = []
     
    def enqueue(self,element):
        
        # FILL OUT CODE HERE
        self.instack.append(element)
    
    def dequeue(self):
        
        # FILL OUT CODE HERE
        if not self.outstack:
        	while self.instack:
        		self.outstack.append(self.instack.pop())
        		
        return self.outstack.pop()

"""
RUN THIS CELL TO CHECK THAT YOUR SOLUTION OUTPUT MAKES SENSE AND BEHAVES AS A QUEUE
"""
q = Queue2Stacks()

for i in xrange(5):
    q.enqueue(i)
    
for i in xrange(5):
    print q.dequeue()