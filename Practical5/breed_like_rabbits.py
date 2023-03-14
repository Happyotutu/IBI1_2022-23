# the number of next generation = 2*the number of this generation
# Every generation, the total number doubles
# while sum<100, keep breeding.


sum=2
#stop when <100, so next generation will >100
n=1
while sum<100:
 sum=sum*2
 n+=1
print("At", str(n), "generation over 100 rabbits have been born.")
