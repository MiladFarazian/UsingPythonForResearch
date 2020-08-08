from collections import Counter

def read_book(title_path):
    """Read a book and return it as a string"""
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def count_words(text):
    """Count the number of times each word occers in text (str). return
    dictionary where keys are unique words and values are word counts. """
    text = text.lower()
    skips = [".",",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts ={}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def word_stats(word_counts):
    """Return number of unique word and word frequencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

text = read_book("./Books/English/Shakespeare/Romeo_and_Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique)
print(sum(counts))

text = read_book("./Books/German/Shakespeare/Romeo_und_Julia.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique)
print(sum(counts))