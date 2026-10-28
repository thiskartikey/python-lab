import string

def get_word_stats(raw_content):
    clean_content = raw_content.lower()
    # Remove punctuation
    clean_content = clean_content.translate(str.maketrans("", "", string.punctuation))
    token_list = clean_content.split()
    word_count = len(token_list)

    # Count word frequency
    freq_map = {}
    for token in token_list:
        freq_map[token] = freq_map.get(token, 0) + 1

    # Detect palindromes
    palindrome_list = []
    for token in freq_map:
        if len(token) > 1 and token == token[::-1]:
            palindrome_list.append(token)

    return word_count, freq_map, palindrome_list

mode = input("Enter F to read a file or M for multiline text: ").strip().upper()

if mode == "F":
    file_path = input("Enter the file name: ")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            document_text = f.read()
        word_count, freq_map, palindrome_list = get_word_stats(document_text)
    except FileNotFoundError:
        print("Error: File not found.")
        exit()
elif mode == "M":
    print("Enter your text.")
    print("Type END on a separate line to finish:")
    collected_lines = []
    while True:
        entry = input()
        if entry == "END":
            break
        collected_lines.append(entry)
    document_text = "\n".join(collected_lines)
    word_count, freq_map, palindrome_list = get_word_stats(document_text)
else:
    print("Invalid choice.")
    exit()

# Display analysis report
print("\n========== TEXT ANALYSIS REPORT ==========")
print("Total Words:", word_count)
print("\nWord Frequency:")
for token in sorted(freq_map):
    print(token, ":", freq_map[token])

print("\nPalindromes:")
if palindrome_list:
    print(", ".join(sorted(palindrome_list)))
else:
    print("No palindromes found.")
print("==========================================")
