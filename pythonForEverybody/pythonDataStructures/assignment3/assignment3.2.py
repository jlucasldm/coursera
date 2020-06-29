#8.5 Open the file mbox-short.txt and read it
# line by line. When you find a line that 
# starts with 'From ' like the following line:

#From stephen.marquard@uct.ac.za Sat Jan  5 09: 14: 16 2008

#You will parse the From line using split() 
# and print out the second word in the line
# (i.e. the entire address of the person who 
# sent the message). Then print out a count 
# at the end.

#Hint: make sure not to include the lines 
# that start with 'From:'.

fname = input("Enter file name: ")
fh = open(fname)
words = list
emails = list()
count = 0

for line in fh:
    if not line.startswith("From"):
        continue
    words = line.split()

    if len(words)>2:
        emails.append(words[1])
        count+=1

for it in emails:
    print(it)

print("There were", count, "lines in the file with From as the first word")
