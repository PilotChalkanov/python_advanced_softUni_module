nums = input().split()
stack =[]
while nums:
    stack.append(nums.pop())
print(" ".join(stack))
