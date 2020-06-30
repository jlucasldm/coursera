# 9.4 Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word 
# of those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail 
# address to a count of the number of times they appear in 
# the file. After the dictionary is produced, the program reads 
# through the dictionary using a maximum loop to find the most 
# prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

words = list()
emails = dict()

for line in handle:
    if not line.startswith("From"):
        continue
    words = line.split()
    if len(words) > 2:
        name = words[1]
        emails[name] = emails.get(name, 0) + 1

bigcount = None
bigword = None
for word,count in emails.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)