# A DNA string is a reverse palindrome if it is equal to its reverse complement.
# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string
# having length between 4 and 12. You may return these pairs in any order.

from util import reverse_complement
from util import exfasta

filepath = "./rosalind_data/rosalind_revp.txt"
fw = list(exfasta(filepath).values())[0]

def main():
    palindromes_positions = {}
    palindromes = {} # not necessary but nice to have
    for x in range(len(fw)):
        for y in range(4, 13):
            current_frame = fw[x:x+y]
            if len(current_frame) in range(4, 13) and current_frame == reverse_complement(current_frame):
                palindromes_positions[x + 1] = len(current_frame) # +1 for human readable lines
                palindromes[current_frame] = len(current_frame)

    for key, value in palindromes_positions.items():
         print(key, value)

if __name__ == "__main__":
    main()