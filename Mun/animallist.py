import sys

animals = ["giraffe","tiger","zebra","elephant","lion"]

data1 = int(sys.argv[1])
data2 = sys.argv[2]


animals.insert(data1,data2) 
del animals[-1]
animals.sort()
print(animals,end="") 

# animals = ["giraffe","tiger","zebra","elephant","lion"]

# print(animals)

# animals.insert(2,"rabbit")
# animals.remove("lion")
# animals.sort()
# print(list(animals)) 