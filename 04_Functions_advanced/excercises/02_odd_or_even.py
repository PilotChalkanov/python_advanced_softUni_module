def odd_even(type, nums):
    parity = 0 if type =='Even' else 1
    result = [el for el in nums if el % 2 == parity]
    return sum(result) * len(nums)
type = input()
nums = [int(x) for x in input().split()]
print(odd_even(type, nums))