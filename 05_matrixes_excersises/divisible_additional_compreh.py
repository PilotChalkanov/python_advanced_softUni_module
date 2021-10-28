start = int(input())
end = int(input())
result = [num for num in range(start,end+1) if [d for d in range(2,11) if num % d] ]
print(result)