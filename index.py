
#Problem 1: Count the number of words in a given text.
text = "Python is easy to learn. Python is useful for AI. Python is popular."

def count_words(text):
    words = text.replace(".", "").split()
    return len(words)

word_count = count_words(text)
print(word_count)

#Problem 2: Count the frequency of each word in a given text.
text = "Python is easy to learn. Python is useful for AI. Python is popular."

def count_words(text):
    words = text.lower().replace(".", "").split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    print(counts)

count_words(text)

#Problem 3: Count the number of words in a given text using a function.
def get_words(text):
    return text.replace(".", "").split()

def count_words(text):
    words = get_words(text)
    return len(words)

text = "Python is easy to learn"

print(count_words(text))