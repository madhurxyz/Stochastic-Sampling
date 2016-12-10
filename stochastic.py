import random
import time
import sys
from histogram import get_words_list
from histogram import create_histogram

def get_random_word(histogram):
    word_list = []
    for key, value in histogram.iteritems():
        word_list.append(key)
    return words_list

def my_app(file_name):
    words_list = get_words_list(file_name)
    histogram = create_histogram(words_list)
    random_word = get_random_word(histogram)



if __name__ == '__main__':
    file_name = str(sys.argv[1])
    my_app(file_name)
