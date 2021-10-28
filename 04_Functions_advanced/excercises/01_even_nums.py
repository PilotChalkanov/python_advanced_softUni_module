def positive_nums(nums):
    return sum([num for num in nums if num >= 0])
def negative_nums(nums):
    return sum([num for num in nums if num < 0])
nums = [int(x) for x in input().split()]
print(negative_nums(nums))
print(positive_nums(nums))

if abs(positive_nums(nums)) > abs(negative_nums(nums)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")