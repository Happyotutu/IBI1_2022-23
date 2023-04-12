seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
TGA_num = seq.count('TGA') #the number of TGA
TAA_num = seq.count('TAA') #the number of TAA
print(TGA_num)
print(TAA_num)
seq_sum = int(TGA_num)+int(TAA_num)
print("Total number of possible coding sequences is", seq_sum)
