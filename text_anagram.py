def clean_string(phrase):
    return "".join(char.lower() for char in phrase if char.isalnum())

def get_signature(phrase):
    sanitized = clean_string(phrase)
    return tuple(sorted(sanitized))

def are_anagrams(str1, str2):
    return get_signature(str1) == get_signature(str2)

def cluster_anagrams(word_list):
    anagram_map = {}
    for word in word_list:
        sig = get_signature(word)
        if sig not in anagram_map:
            anagram_map[sig] = []
        anagram_map[sig].append(word)
    return anagram_map

first_input = input("Enter first word or phrase: ")
second_input = input("Enter second word or phrase: ")

if are_anagrams(first_input, second_input):
    print("The two texts are anagrams.")
else:
    print("The two texts are not anagrams.")

words_entered = input("\nEnter multiple words separated by spaces: ").split()
clusters = cluster_anagrams(words_entered)

print("\nAnagram Groups:")
for key_sig, group in clusters.items():
    print(group)
