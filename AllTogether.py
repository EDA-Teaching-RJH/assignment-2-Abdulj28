### Part Four -- your code goes here. 
import random


rlist = random.sample(range(1,100), 10)

print(rlist)


nlist = [i for i in rlist if i % 2 != 0]
print(nlist)
