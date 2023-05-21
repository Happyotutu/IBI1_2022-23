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
    code_seq = coding_seq+"TGA" 
    print("The length of coding line is", len(code_seq))
    per = len(code_seq)/len(self)
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
#an example
#Please input a DNA sequence: AAAAAAAATTTTTTATGCCCCGGGGGAAATTTTTGAAAAAAA
#The length of coding line is 22
#The percent of coding sequence is 52%
#This sequence is a protein-coding sequence.
