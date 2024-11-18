# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from
# the original file. Assume 1-based numbering of lines.


# FOR OUTPUT USE SHELL DIRECTION
# execute on command line as following:
# python ini5.py > ini5_solution.txt

open("ini5_solution.txt")
filepath = "./rosalind_data/rosalind_ini5.txt"
with open(filepath, "r") as infile:
    line_object = infile.readlines()
    for lines in line_object[1::2]:
        print(lines.rstrip())


#write out to file
#with open("some_path.txt", "w") as outfile:
#    outfile.write(string + "\n")