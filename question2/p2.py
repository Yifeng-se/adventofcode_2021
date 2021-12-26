file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
horizontal = 0
depth = 0

for line in Lines:

    sCurr = line.strip()

    if sCurr[:3] == "for":
    	horizontal += int(sCurr[8:])
    elif sCurr[:3] == "dow":
    	depth += int(sCurr[5:])
    elif sCurr[:3] == "up ":
    	depth -= int(sCurr[3:])
    	

print(str(horizontal*depth))