from collections import Counter, deque

# n = int(input())
n = 4
words = deque([])

# Input words
for _ in range(n):
    word = input()
    words.append(word)

# Count occurrences of words using Counter
word_counts = Counter(words)

# Print the number of distinct words
distinct_words = len(word_counts)
print(distinct_words)

# Print the counts of each distinct word
for word, count in word_counts.items():
    print(count, end=' ')

