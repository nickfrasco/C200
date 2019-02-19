
class CCPlate:
    def __init__(self,size,color):
        self.size = size
        self.color = color
    def c(self):
        return self.color
    def s(self):
        return self.size
    def __str__(self):
        return str(self.color) + " " + str(self.size)
    def __repr__(self):
        return str(self.color) + " " + str(self.size)

class Stack:
   def __init__(self):
      self.stack = []
   def isEmpty(self):
      return self.stack == []
   def push(self, item):
      self.stack.insert(0,item)
   def pop(self):
      x = self.stack[0]
      self.stack.remove(x)
      return x
   def size(self):
      return len(self.stack)
   def peek(self):
      return self.items[len(self.items)-1]
   def __str__(self):
      return str(self.stack)

def transfer(a, b, c):
    organized = False
    while not organized:
        pole3.push(pole2.pop())
        pole3.push(pole1.pop())
        pole2.push(pole3.pop())
        pole2.push(pole3.pop())
        pole3.push(pole1.pop())
        pole1.push(pole2.pop())
        pole1.push(pole2.pop())
        pole3.push(pole2.pop())
        pole3.push(pole1.pop())
        pole3.push(pole1.pop())
        pole1.push(pole2.pop())
        pole1.push(pole3.pop())
        pole1.push(pole3.pop())
        pole2.push(pole3.pop())
        pole2.push(pole3.pop())
        pole2.push(pole1.pop())
        pole2.push(pole1.pop())
        pole3.push(pole1.pop())
        pole3.push(pole1.pop())
        pole1.push(pole2.pop())
        pole1.push(pole2.pop())
        pole3.push(pole2.pop())
        pole3.push(pole2.pop())
        pole2.push(pole1.pop())
        pole2.push(pole1.pop())
        pole1.push(pole3.pop())
        pole1.push(pole3.pop())
        pole1.push(pole2.pop())
        pole1.push(pole2.pop())
        pole2.push(pole3.pop())
        pole2.push(pole3.pop())
        pole2.push(pole1.pop())
        pole2.push(pole1.pop())
        pole3.push(pole1.pop())
        pole3.push(pole1.pop())
        pole3.push(pole2.pop())
        pole3.push(pole2.pop())
        pole1.push(pole2.pop())
        pole1.push(pole3.pop())
        pole1.push(pole3.pop())
        pole2.push(pole3.pop())
        pole2.push(pole1.pop())
        pole2.push(pole1.pop())
        pole1.push(pole3.pop())
        pole3.push(pole2.pop())
        pole1.push(pole2.pop())
        pole2.push(pole3.pop())
        organized = True

pole1, pole2, pole3 = Stack(), Stack(), Stack()

print(pole1, pole2, pole3)

for i in range(4,0,-1):
    pole1.push(CCPlate(i,i%2*"cream" or "crimson"))
for i in range(4,0,-1):
    pole2.push(CCPlate(i,i%2*"crimson" or "cream"))

print(pole1, pole2, pole3)
transfer(pole1, pole2, pole3)
print(pole1, pole2, pole3)




