import re
regex1 = "[A-z]"
regex2 = "[^\w\s]"
counter = 0
with open("text.txt",'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        print(lines[i])
        matches1 = re.findall(regex1,lines[i])
        matches2 = re.findall(regex2,lines[i])
        print(f"Line {i}: {lines[i]} ({len(matches1)})({len(matches2)})")
