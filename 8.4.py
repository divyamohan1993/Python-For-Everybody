# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output. You can download the sample data at http://www.py4e.com/code3/romeo.txt

# DO NOT COPY THE SOLUTION. ACTIONS MIGHT BE TAKEN ON YOUR ACCOUNT.

#fname = input("Enter file name: ")
fname = 'romeo.txt'
fh = open(fname)
lst = list()
data = ''
for line in fh:
    data = line.split()
    # print(data)
    for dat in data:
        #print(dat)
        if dat not in lst:
            lst.append(dat)
    
lst.sort()    
print(lst)
