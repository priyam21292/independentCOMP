genetic_code= {	'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
				'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
				'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
				'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
				'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
				'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
				'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
				'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
				'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
				'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
				'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
				'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
				'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
				'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
				'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
				'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def protein_translation( seq, genetic_code):
	protein_seq=''
	for i in range (0, len(seq), 3 ):
		codon= seq[i:i+3]
		protein_seq += genetic_code[ codon ]
	return protein_seq

print(protein_translation( "ATGCTACTCTAG", genetic_code))