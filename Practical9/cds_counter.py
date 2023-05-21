seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
TGA_num = seq.count('TGA') #the number of TGA
TAA_num = seq.count('TAA') #the number of TAA
TAG_num = seq.count('TAG') #the number of TAG
#print(TGA_num)
#print(TAA_num)
#print(TAG_num)
seq_sum = int(TGA_num)+int(TAA_num)+int(TAG_num)
print("Total number of possible coding sequences is", seq_sum)
