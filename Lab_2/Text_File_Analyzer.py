from collections import Counter

# Open and Read the Text File
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Trying the function
content = read_file('sample.txt')
print(content[:100])   # Print the first 100 characters

# Counting the Number of Lines
def count_line(content):
    return len(content.split('\n'))  # Fixed newline character

# Counting Words
def count_word(content):
    return len(content.split())

# Finding the Most Common Word
def most_common_words(content):
    word = content.lower().split()
    word_count = Counter(word)
    return word_count.most_common(1)[0]

# Calculating Average Words Length
def average_words_length(content):
    word = content.split()
    total_Length = sum(len(words) for words in word)
    return total_Length / len(word)

# Question 1: Modify the program to count the number of unique words in the text
def count_unique_word(content):
    word = content.lower().split()
    unique_word = set(word)
    return len(unique_word)

# Question 2: Add a function to find the longest word in the text.
def long_words(content):
    word = content.split()
    return max(word, key=len)

# Question 3: Implement a feature to count the occurrences of a specific word (case-insensitive).
def counting_specfic_words(content, target_words):
    word = content.lower().split()
    return word.count(target_words.lower())

# Question 4: Create a function to calculate the percentage of words that are longer than the average word length.
def percentage_of_words_longer_than_average(content):
    word = content.split()
    average_length = average_words_length(content)
    longer_word = [words for words in word if len(words) > average_length]
    return (len(longer_word) / len(word)) * 100

# Analyzation 
def analyze_sample_text(filename):
    content = read_file(filename)

    number_of_line = count_line(content)
    number_of_word = count_word(content)
    common_words, count = most_common_words(content)
    average_length = average_words_length(content)
    number_of_unique_word = count_unique_word(content)
    long_word = long_words(content)
    specific_words_counting = counting_specfic_words(content, 'Finn')  # Added 'Finn' as a specific word
    percentage = percentage_of_words_longer_than_average(content)
    
    # Results
    print(f"File: {filename}")
    print(f"Number of lines: {number_of_line}")
    print(f"Number of words: {number_of_word}")
    print(f"Most common word: '{common_words}' (appears {count} times)")
    print(f"Average word length: {average_length:.2f} characters")
    print(f"Number of unique words: {number_of_unique_word}")
    print(f"Longest word: {long_word}")
    print(f"Occurrences of the word 'Finn': {specific_words_counting}")
    print(f"Percentage of words longer than average: {percentage:.2f}%")

# Running the analysis on 'sample.txt'
analyze_sample_text('sample.txt')
