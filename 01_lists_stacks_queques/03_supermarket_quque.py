from collections import deque

queque = deque()
people = input()

while people != 'End':    
    if people == 'Paid':
        while queque:
            print(queque.popleft())
    else:
        queque.append(people)
    people = input()

print(f"{len(queque)} people remaining.")


     
    
        
        
     
    


