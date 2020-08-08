text = "This is my test text. We're keeping this text short to keep things manageable"

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

from collections import Counter

def count_words_fast(text):
    """Count the number of times each word occers in text (str). return
    dictionary where keys are unique words and values are word counts. """
    text = text.lower()
    skips = [".",",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

print(count_words_fast(text))
print(count_words_fast(text) is count_words(text))

print(len(count_words("This comprehension check is to check for comprehension.")))