import sys


file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
count = 0
iIncrease = 0
input_list = []

# Strips the newline character
for line in Lines:
    input_list.append(line.strip())

for i in range(len(input_list) - 2):
    if i == 0:
        iPre = int(input_list[i]) + int(input_list[i + 1]) + int(input_list[i + 2])
    else:
        iCurr = int(input_list[i]) + int(input_list[i + 1]) + int(input_list[i + 2])
        if iCurr > iPre:
            iIncrease += 1
        iPre = iCurr

print(iIncrease)
