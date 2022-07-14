#grc exercise to count words in a file and write the word frequencies
import os
import re
from collections import Counter


def count_words(ftext):
    """" use Counter to count word freq based on whitespace:
    arg: str (full text) --- return: Counter """
    full_text = re.findall("\w+", ftext.lower().strip())
    ##full_text: list = ftext.lower().rstrip().split()  #strip whitespace, convert to lowercase, returns as list
    print(full_text)  #debug
    word_count_counter = Counter(full_text)
    return word_count_counter


def read_write(in_fname, out_fname):
    if os.path.isfile(in_fname):
        with open(in_fname, 'r') as in_fh:
            ftext = in_fh.read()
        counted_words = count_words(ftext)
        print(counted_words)  #debug
        for key in counted_words.keys():
            print(f'{key}: {counted_words[key]}')

        with open(out_fname, 'w') as out_fh:
            for word, count in counted_words.items():
                out_fh.write(f"{word},{count}\n")
    else:
        print("invalid file")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #TODO remove punctuation marks and eol eg 'day' should be 3
    #TODO
    read_write("../data/simple_file.txt", "../data/simple_counts.txt")
