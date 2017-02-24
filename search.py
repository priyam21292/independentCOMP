'''
This program mainly focuses on the sequence binding to 
the probe in microarray experiment. But the end result 
is produced as the compliment of the sequence.

First, the program will search for the query in the sequence 
and store its index position. Once the match is found, the loop 
exits and the second part of the program will produce the compliment 
of sequence starting from that index position.
'''

sequence = 'AATGTTTACCCGGCCGGCGCCGGAAATGCTTAGTAGCGTTGGCGG'
search = 'CGGAAATGC'

print ("Sequence: ", sequence)
print ("Search sequence: ", search)
index = 0
length = len(sequence)
probe = ''
for i in range(len(sequence)-len(search)+1):
	if (search == sequence[i:i+len(search)]):
		index = i
		break
print ("\nIndex position found: ",index)		

for i in range(index,length):
	if (sequence[i] == 'A'):
		probe = probe + 'T'
	elif (sequence[i] == 'T'):
		probe = probe + 'A'
	elif (sequence[i] == 'G'):
		probe = probe + 'C'
	else:
		probe = probe + 'G'
print ("\nComplimentary sequence: ", probe)