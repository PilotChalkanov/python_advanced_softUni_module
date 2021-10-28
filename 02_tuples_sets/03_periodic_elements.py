n = int(input())
elements = []
for _ in range(n):
    elements.append(input().split())
elements_flat = [el for sublist in elements for el in sublist]
elements_set = set(elements_flat)
print("\n".join(elements_set))