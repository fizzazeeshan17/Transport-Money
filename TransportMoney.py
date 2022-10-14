# Declare varibales

small_bag = 20
medium_bag = 50
big_bag = 80
small_bag_cost = 10000
medium_bag_cost = 30000
big_bag_cost = 60000
numbBag = 0
nummBag = 0
numsBag = 0

# Allow the user to enter input

print('Welcome to the Money Bag Transport Calculator (M.B.T.C')
print('-------------------------------------------------------')
print()
volume = int(input('What is the volume of the truck (>=100L):'))
while not volume >= 100:
    volume = int(input('What is the volume of the truck (>=100L):'))
print()
print('Packing plan')
print('-------------')

# Number of bags that will fit in the truck

# Big bag
while volume > big_bag:
    numbBag = int(volume / big_bag)
    remainder = volume % big_bag
    break

# Medium bag
while remainder >= medium_bag:
    nummBag = int(remainder / medium_bag)
    remainder = remainder % medium_bag
    break

# Small bag
while remainder >= small_bag:
    numsBag = int(remainder / small_bag)
    break
# Print calculations

print(numbBag, 'big bags')
print(nummBag, 'medium bags')
print(numsBag, 'small bags')
print()


# Space left in the truck

spacenumbBag = big_bag * numbBag
spacenummBag = medium_bag * nummBag
spacenumsBag = small_bag * numsBag
space_left = int(volume-spacenumbBag-spacenummBag-spacenumsBag)

print(f'Space left(L) : {space_left}L')

# Print total

totalnumbBag = big_bag_cost * numbBag
totalnummBag = medium_bag_cost * nummBag
totalnumsBag = small_bag_cost * numsBag
total_value = totalnumbBag + totalnummBag + totalnumsBag

print(f'Total value: {total_value}kr')

# The End
