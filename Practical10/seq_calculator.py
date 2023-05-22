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
    len_code_seq = len(coding_seq)-3
    print("The length of coding line is", len_code_seq)
    per = len_code_seq/len(self)
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
#Please input a DNA sequence: AAAAAAAATTTTTTATGCCCCGGGGGAAATTTTTGAAAAAAA
#The length of coding line is 16
#The percent of coding sequence is 38%
#This sequence is an unclear sequence.
