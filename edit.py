'''
The minimum edit distance ED(x,y) between two strings (x & y) is minimum number of operations needed
to transform one into the other 

Operations - 
	- Insertion
	- Deletion
	- Substitution

For example, 

x = ATGCA
y = TGCA
ED(x,y) = 1		Deletion of A from x.

x = ATTGCGA
y = TAGC
ED(x,y) = 4		Delete A, substitute T with A and, delete G and A

ED(i,j) is computed by the following -

If x[i] == y[j], ED(i,j) = ED(i-1,j-1)

If x[i] != y[j] 	the minimum of the below is considered
ED(i,j) = ED(i-1,j) + 1			Deletion
ED(i,j) = ED(i,j-1) + 1			Insertion
ED(i,j) = ED(i-1,j-1) + 1		Substitution
'''

x = 'ATTGCGA'
y = 'TAGC'

table = {}
def ED(x,y,i,j):
	if (i,j) in table:
		return table[(i,j)]
	if i<0:
		table[(i,j)] = j+1
		return j+1
	if j<0:
		table[(i,j)] = i+1
		return i+1
	if x[i] == y[j]:
		table[(i,j)] = ED(x,y,i-1,j-1)
		return table[(i,j)]
	else:
		table[(i,j)] = min(ED(x,y,i,j-1)+1, ED(x,y,i-1,j)+1, ED(x,y,i-1,j-1)+1)
		return table[(i,j)]

print(ED(x,y,len(x)-1, len(y)-1))


'''
Some inputs for this code - 
x = 'TGCATAT'
y = 'ATCCGAT'

x = 'ATATATAT'
y = 'TATATATA'
'''

