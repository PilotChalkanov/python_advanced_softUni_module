n = int(input())
name_set = set()
for _ in range(n):
    name = input()
    name_set.add(name)
print("\n".join(name_set))