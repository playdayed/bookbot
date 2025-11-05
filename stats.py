def wordcount(file_contents):
		words = file_contents.split()
		print (f"Found {len(words)} total words")

def letters(file_contents):
    lower_text = file_contents.lower()
    letter_counts = {}

    for char in lower_text:
        if char.isalpha():  # only count letters
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

    return letter_counts


def bookreport(letter_counts):
    # Convert dictionary into a list of (letter, count) pairs
    sorted_letters = sorted(letter_counts.items(), key=lambda item: item[1], reverse=True)

    # Print results
    for char, count in sorted_letters:
        print(f"{char}: {count}")
    return
