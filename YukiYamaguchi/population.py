import sys
args = sys.argv
pos = int(args[1])

# make a list of population rank
countries = ("China","India","U.S.A","Indnesia","Pakistan","Brazili","Nigeria","Bangladesh","Russia","Mexico")

# pick and show the country's name that pointed by args
print(countries[pos-1],end="")