import random
lst = []
for i in range(1000000):
	lst.append(i)
	a = random.choice(lst)
print(a)
