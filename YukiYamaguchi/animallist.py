import sys
args = sys.argv
pos = int(args[1])
new = str(args[2])

animal_list = ["giraffe", "tiger", "zebra", "elephant", "lion"]

animal_list.insert(pos, new)


del animal_list[-1]

animal_list.sort()

print(animal_list, end="")