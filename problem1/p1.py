import sys


file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0
iIncrease = 0

# Strips the newline character
for line in Lines:
    count += 1

    iCurr = int(line.strip())

    if count == 1:
    	iPre = iCurr
    else:
    	if iCurr > iPre:
    		iIncrease += 1
    	

    print(str(iPre) + " " + str(iCurr) + " " + str(count) + " " + str(iIncrease))
    iPre = iCurr

print(iIncrease)
