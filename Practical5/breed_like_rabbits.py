# the number of next generation = 2*the number of this generation
# Every generation, the total number doubles
# while sum<100, keep breeding.

#Repeat
#      breeding
#      How many rabbits in total?
#        If less than 100, keep breeding
#        Once more than 100, stop
#    ! Stop when less than 100, so the generation should plus 1 to exceed 100

sum=2 #initial number of rabbits
#stop when <100, so next generation will >100
n=1 # generation number
while sum<100:
 sum=sum*2 #the number of next generation = 2*the number of this generation
 n+=1
print("At", str(n), "generation over 100 rabbits have been born.")

# At 7 generation over 100 rabbits have been born.

