# the length of enconding sequence contains ATG, didn't contain TGA

def DNA_cal(self):
    """
    When meet ATG, start counting. 
    When meet TGA, stop counting
    per = count/len(self)
    if pre >= 50% print('protein-coding')
    if pre <= 10% print('non-coding')
    else print('unclear')
    
    """
    sequence = self.upper()
    start_seq = sequence[sequence.index("ATG"):]
    coding_seq = start_seq[:start_seq.index("TGA")]
    print("The length of coding line is", len(coding_seq))
    per = len(coding_seq)/len(self)
    percent = '{:.0%}'.format(per)
    print("The percent of coding sequence is", percent)
    return per

seq = input("Please input a DNA sequence:")
per = DNA_cal(seq)
if per > 0.5:
   print("This sequence is a protein-coding sequence.")
elif per < 0.1:
    print("This sequence is a non-coding sequence.")
else:
    print("This sequence is an unclear sequence.")
#my example
#Please input a DNA sequence: AAAAAAAATTTTTATGCCCCGGGGAAATTTTTGAAAAAAA
#The length of coding line is 18
#The percent of coding sequence is 45%
#This sequence is an unclear sequence.
