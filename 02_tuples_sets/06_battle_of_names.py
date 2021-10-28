import math
n = int(input())
odd_ascii_sums = set()
even_ascii_sums = set()
for i in range(1, n+1, 1):
    line = input()
    current_sum = math.floor(sum([ord(char) for char in line])/i)
    odd_ascii_sums.add(current_sum) if current_sum % 2 == 1 else even_ascii_sums.add(current_sum)
if sum(odd_ascii_sums) == sum(even_ascii_sums):
    print(", ".join(str(x) for x in odd_ascii_sums.union(even_ascii_sums)))
elif sum(odd_ascii_sums) > sum(even_ascii_sums):
    print(", ".join(str(x) for x in odd_ascii_sums.difference(even_ascii_sums)))
else:
    print(", ".join(str(x) for x in odd_ascii_sums.symmetric_difference(even_ascii_sums)))
