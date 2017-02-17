'''
This program works on the idea of edit distance. The only difference is assigning gap penalty for each gap.
Also penlaty for each insertion/deletion or substitution.
The penalty for insertion/deletion is kept higher because we want to avoid that.
Therefore the else statement chooses the max of substitution, insertion or deletion.
The objective is to find the optimal alignment score for the two input sequences.
Additional iputs: "AAATGTGTTTTTTTCGCGGGTGAAACA"
				  "TTTTTGCGGGCGGGAGGGAGGGGCG"
'''

seq1="ATGCCGATAAATTCCCCGCGCGGTGGT"			# Input Sequence 1
seq2="AATTTTGGTTCGAATTTGTTTGGTTCGCG"		# Input Sequence 2

i = len(seq1)-1	# Length of Sequence 1
j = len(seq2)-1	# Length of Sequence 2

match=1				# Score for match
substitution=-3		# Substitution Score
insert_delete=-5	# Insertion or deletion score


Table={}
def Alignment(x,y,i,j):
	if (i,j) not in Table:
		if i==-1:
			Table[i,j]= insert_delete*(j+1)
		elif j==-1:
			Table[i,j]= insert_delete*(i+1)
		elif x[i]==y[j]:
			Table[i,j]= match + Alignment(x,y,i-1,j-1)
		# if no match, assign the max score between substitution, insertion or deletion
		else:
			Table[i,j]= max(substitution+Alignment(x,y,i-1,j-1),insert_delete+Alignment(x,y,i-1,j),insert_delete+Alignment(x,y,i,j-1))  

	return Table[i,j]

print(Alignment(seq1,seq2,i,j))