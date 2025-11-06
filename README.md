# 📘 BookBot

BookBot is my first project from [Boot.dev](https://www.boot.dev)!  
It’s a command-line Python program that analyzes books and reports useful statistics like total word count and letter frequency.

---

## 🚀 Features
- Reads any `.txt` file passed as a command-line argument  
- Counts total words in the book  
- Counts how many times each letter appears (case-insensitive)  
- Sorts and displays the most common letters  
- Handles multiple books from the `books/` directory (e.g., *Frankenstein*, *Moby Dick*, *Pride and Prejudice*)

---

## 🧠 How It Works
1. **`main.py`** handles reading the file and command-line arguments.  
2. **`stats.py`** contains helper functions:
   - `wordcount()` → counts words  
   - `letters()` → counts each letter  
   - `bookreport()` → prints a formatted summary of letter frequencies  

---

## ⚙️ Usage

### 1️⃣ Run with a Book File
bash
```
python3 main.py books/frankenstein.txt
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75,767 total words
--------- Character Count -------
't': 29,493
'h': 19,176
'e': 44,538
... (and so on)
============= END ===============
```

### 1️⃣ Run with a Book File
bookbot/
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
├── main.py
├── stats.py
└── README.md
