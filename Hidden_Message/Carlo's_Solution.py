"""You are working with a team of genetics researchers. You're told the exciting and confusing news that there may be a message from God hidden in our DNA! Through science and prayer your team has been able to work out the following:
* The message is hidden somewhere in the attached sequence of ~120,000 base pairs
* God writes in stochastic binary, with 0 represented by either A or C, and 1 represented by either T or G
* God encodes in ASCII
Can you find the message?"""

# Importing the libraries
from Bio import SeqIO

# Importing the dataset
record = SeqIO.read("id100228968.seq", "fasta")

# Descriptors of the dataset
print("ID %s" % record.id)
print("Sequence length %i" % len(record))
print(record)
print(record[0:1])

# Translating DNA code to Binary
translated = []
for i in range(len(record)):
    if record[i] == 'A':
        translated.append(str(0))
    elif record[i] == 'C':
        translated.append(str(0))
    elif record[i] == 'T':
        translated.append(str(1))
    elif record[i] == 'G':
        translated.append(str(1))

# Translated data in a list, separated by commas
print(translated)

# Joined the components of the list and combined into one string, getting rid of the commas
bitstring = "".join(translated)
print(bitstring)

# Translate from binary to ASCII
bitstring = bitstring[2:]
bitstring = -len(bitstring) % 8 * '0' + bitstring

# Frameshifts, positions 1 to 7
for j in range(7):
    string_blocks = (bitstring[(i+j):(i+8+j)] for i in range(0, len(bitstring), 8))
    string = ''.join(chr(int(char, 2)) for char in string_blocks)
    print (' ')
    print('frameshift' + ' ' + str(j))
    print (' ')
    print(string)

# Looking at printout shows the message from God in frameshift #3
