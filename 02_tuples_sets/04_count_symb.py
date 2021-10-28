word = input()
dict_chars = {}
for char in word:
    if char not in dict_chars:
        dict_chars[char] = 1
    else:
        dict_chars[char] +=1

sorted_dict = sorted(dict_chars.items(),)
[print(f"{el[0]}: {el[1]} time/s") for el in sorted_dict]

