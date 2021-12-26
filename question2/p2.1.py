file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
horizontal = 0
depth = 0
aim = 0

for line in Lines:

    sCurr = line.strip()

    if sCurr[:3] == "for":
        horizontal += int(sCurr[8:])
        depth += int(sCurr[8:]) * aim
    elif sCurr[:3] == "dow":
    	aim += int(sCurr[5:])
    elif sCurr[:3] == "up ":
    	aim -= int(sCurr[3:])
    	

print(str(horizontal*depth))