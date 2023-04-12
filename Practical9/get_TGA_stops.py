output_file = open('TGA_genes.fa',"w") 
content = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
print(content)
gene_name = ''
sequence = ''
for line in content:
  if line.startswith('>'):
      if sequence.endswith('TGA'):
        output_file.write(f'>{gene_name}\n{sequence}\n')
      gene_name=line.strip().split()[0][1:]
      sequence = ''
  else:
      sequence += line.strip()
output_file.close()

