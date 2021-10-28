clothes = input().split()
rack_capacity = int(input())
rack_count = 0
current_capacity = 0
is_empty = False
while clothes:
    rack_count +=1
    current_capacity = int(clothes.pop())
    if clothes:
        while current_capacity+int(clothes[-1]) <= rack_capacity:        
            current_capacity += int(clothes.pop())  
            if not clothes:
                break
    
print(rack_count)