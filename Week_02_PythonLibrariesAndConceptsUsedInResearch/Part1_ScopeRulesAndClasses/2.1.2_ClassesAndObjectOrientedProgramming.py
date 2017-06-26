class NewList(list):
   def remove_max(self):
     self.remove(max(self))
   def append_sum(self):
     self.append(sum(self))

x = NewList([4,8,9])
print(x)
print(max(x))
while max(x) < 10:
   x.remove_max()
   x.append_sum()
print(x)

