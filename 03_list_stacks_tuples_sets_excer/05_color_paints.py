from collections import deque
import math
color_str = deque(input().split())

colors_primary = ['red','yellow','blue']
colors_second = ['orange', 'purple', 'green']
result = []
while len(color_str) >1:
    left_subs = color_str.popleft()
    right_subs = color_str.pop()
    word1 = left_subs+right_subs
    word2 = right_subs + left_subs
    if word1 in colors_primary or word1 in colors_second:

        result.append(word1)
    elif word2 in colors_primary or word2 in colors_second:

        result.append(word2)
    elif word1 and word2 not in colors_primary and word1 and word2 not in colors_second:
       left_subs = left_subs[0:-1]
       right_subs = right_subs[0:-1]
       color_str.insert(math.floor(len(color_str)/2), left_subs)
       color_str.insert(math.floor(len(color_str)/2), right_subs)

if "orange" in result:
    if "red" and "yellow" not in result:
        result.remove("orange")

elif "purple" in result:
    if "red" and "blue" not in result:
        result.remove("purple")
elif "green" in result:
    if "yellow" and "blue" not in result:
        result.remove("green")
print(result)