def palindrome(word,init_index):
   if init_index == len(word)//2:
       return f"{word} is a palindrome"

   last_index = len(word) - 1 - init_index
   if word[init_index] != word[last_index]:
       return f"{word} is not a palindrome"
   return palindrome(word, init_index + 1)




print(palindrome("abcdcba", 0))
print(palindrome("peter", 0))