# What does this piece of code do?
# Answer: Randomly generate 9 numbers in (1,100) and print out the biggest one

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0
stored_random_number=0
while progress<10:
#create a  loop
	progress+=1
	n = randint(1,100)
        #produce a random number in (1,100)
	if n > stored_random_number:  # stored_random_number = Max{n, stored_random_number}
		stored_random_number = n

print(stored_random_number)
