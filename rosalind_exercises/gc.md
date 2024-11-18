## Rosalind: Computing GC Content
_**Given:** At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
**Return:** The ID of the string having the highest GC-content, followed by the GC-content of that string._

------------------------------------------------

open input = fasta file.
strip all lines contained, return them in list

with loop, go through all lines in stripped list.  
make a list containing the dna indices.  
make a list containing the concatenated dna strings.

```python
for lines in read_input(filepath):
    if they contain ">":
        put them in index list
    else:
        concatenate non > containing lines into one string and put it into strings list
    this else loop will run until the next line with ">" comes => this way, we get two lists, and dna and index at their respective positions match each other
```

then make a dna dictionary:
with for loop, match indeces + strings together

```python
for range(len(index))
    dnadict[index_list[x]] = strings_list[x]
```

define a gc-computing function:
```python
def gccomp(x):
    gccount = 0
    atcount = 0
    for position in range(len(x)):
        if x[position] == "A" or x[position] == "T":
            atcount += 1
        else:
            gccount += 1
    return((gccount / (atcount + gccount)) * 100)
```

apply gc function to all values in the dictionary, then get the highest one + print it with the respective index

```python
for key in dnadict.keys():
    dnadict[key] = gccomp(dnadict[key])

for key in dnadict.keys():
    if dnadict[key] == max(dnadict.values()):
        print(key.lstrip(">"))
        print(dnadict[key])
```



