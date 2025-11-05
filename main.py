from sys import *
from stats import wordcount, letters, bookreport



def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents
		
		
def main():
	path = argv[1]
	text = get_book_text(path)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	wordcount(text)
	print("--------- Character Count -------")
	letter_count = letters(text)
	bookreport(letter_count)
	print("============= END ===============")


if len(argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	exit(1)
elif len(argv) == 2:
	main()

