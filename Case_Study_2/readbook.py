def read_book(title_path):
    """Read a book and return it as a string"""
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

text = read_book("Romeo_and_Juliet.txt")
print(len(text))
print(text.find("What's in a name"))