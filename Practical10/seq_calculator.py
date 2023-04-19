def DNA_cal(self):
    """
    When meet ATG, start counting. 
    When meet TGA, stop counting
    per = count/len(self)
    if pre >= 50% print('protein-coding')
    if pre <= 10% print('non-coding')
    else print('unclear')
    
    """
    start_seq = self[self.index("ATG"):]
    coding_seq = start_seq[:start_seq.index("TGA")]
    code_seq = coding_seq+"TGA" 
    print("The length of coding line is", len(code_seq))
    per = len(code_seq)/len(self)
    percent = '{:.0%}'.format(per)
    print("The percent of coding sequence is", percent)
    if per > 0.5:
        print("This sequence is a protein-coding sequence.")
    if per < 0.1:
        print("This sequence is a non-coding sequence.")
    else:
        print("This sequence is an unclear sequence.")
seq = input("Please input a DNA sequence:")
DNA_cal(seq)
