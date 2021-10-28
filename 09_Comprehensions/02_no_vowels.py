word = input()
vowel_list = ['A', 'E', 'I', 'O', 'U','a','e', 'i','o','u']
print("".join([ch for ch in word if ch not in vowel_list]))

def is_vowel(character):
    if character.lower in "aeouie":
        return True
    return False

print("".join([char for char in input() if not is_vowel(char)]))