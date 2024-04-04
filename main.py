"""
This program reads the text from the file books/frankenstein.txt and displays a report of the text.

Author: Chris H.
GitHub: github.com/crhowell
"""

def count_letters(text):
    """
    Count the occurences of each letter in the text.

    Args:
    text: str: The text to count the letters in.

    Returns:
    dict: A dictionary with the letters as keys and the counts as values.
    """
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

def count_words(text):
    """
    Count the number of words in the text (separated by spaces).

    Args:
    text: str: The text to count the words in.

    Returns:
    int: The number of words in the text.
    """
    return len(text.split()) 


def display_report(text):
    """
    Display a report of the text, including the number of words and the number of each letter.

    Args:
    text: str: The text to display the report of.

    Returns:
    None
    """
    word_count = count_words(text)
    letter_counts = count_letters(text)
    sorted_counts = sorted(letter_counts, key=letter_counts.get, reverse=True)
    counts = [{"letter": k, "count": letter_counts[k]} for k in sorted_counts]

    print("-- Report of books/frankenstein.txt --")
    print(f"Number of words: {word_count}\n")

    for count in counts:
        print(f'Number of the letter \'{count["letter"]}\' found: {count["count"]}')
    print("-- End of report --")


def main():
    with open('books/frankenstein.txt', 'r') as file:
        # read the entire text.
        text = file.read()
        # display the report to stdout.
        display_report(text)
    # program completed.

if __name__ == '__main__':
    main()
