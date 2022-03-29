#create an empty set
s = set()

s.add(1)
s.add(3)
s.add(2)
s.add(4)
s.add('article')
s.add(4)
s.remove(4)

print(s)
print(f"This sets has {len(s)} elements")