# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# DO NOT COPY THE SOLUTION. ACTIONS MIGHT BE TAKEN ON YOUR ACCOUNT.

#name = input("Enter file:")
# if len(name) < 1:
name = "mbox-short.txt"
handle = open(name)
maildict = {}
for lines in handle:
    if not lines.startswith('From:'):
        continue
    # print (lines)
    email = lines.split()[1]
    maildict[email] = maildict.get(email,0) + 1
       
#print(maildict)

key = None
value = None

for mail,times in maildict.items():
    if value is None or times > value:
        key = mail
        value = times

print(key, value)
    