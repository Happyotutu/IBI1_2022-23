content = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
print(content)
stop_codons = input("Please input 'TAA', 'TAG' or 'TGA':")
output_file = open(stop_codons+"_stop_genes.fa", 'w')
gene_name = '' #as a variable to store gene name
sequence = '' #as a variable to store sequence
for line in content:
  if line.startswith('>'):
      if sequence and sequence.endswith(f'{stop_codons}'):
          number = str(sequence.count(stop_codons))
          output_file.write(f'>{gene_name}{number}\n{sequence}\n')
      sequence = ''
      gene_name=line.split()[0] + " the number of coding sequences is :" 
  else:
      sequence += line.strip()
output_file.close()

