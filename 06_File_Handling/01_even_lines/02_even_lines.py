import re
regex = "[^\w\s]"
counter = 0
with open ("text.txt", 'r') as file:
    lines = file.readlines()
    for line_num in range(0,len(lines),2):

        text_list = list(reversed(lines[line_num].split()))
        line_back_reversed = " ".join(text_list)
        subs_line = re.sub(regex,'@',line_back_reversed)
        print(subs_line)
