import sys
import string
from collections import Counter
import string
import matplotlib.pyplot as plt  # Only if you do the stretch goal

def load_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def clean_text(text):
    return ''.join(char.lower() for char in text if char not in string.punctuation)

def analyze_text(text):
    words = text.split()            # splits on any whitespace
    lines = text.splitlines()        # splits on newlines
    characters = len(text)           # counts all characters

    print(f"Total words: {len(words)}")
    print(f"Total lines: {len(lines)}")
    print(f"Total characters: {characters}")

def most_common_words(words, n=5):
    counter = Counter(words)
    return counter.most_common(n)

def plot_common_words(common_words):
    words = [word for word, count in common_words]
    counts = [count for word, count in common_words]
    
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title('Top Common Words')
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python text_analyzer.py filename.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    text = load_text(filename)
    cleaned_text = clean_text(text)
    words = cleaned_text.split()

    analyze_text(cleaned_text)
    common_words = most_common_words(words)

    print("\nTop common words:", common_words)  # Good to show this in terminal
    plot_common_words(common_words)

if __name__ == "__main__":
    main()
