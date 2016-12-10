import random
import time
import sys
from histogram import get_words_list
from histogram import create_histogram

def get_count(histogram):
    count = 0
    for key,value in histogram.iteritems():
        count += value
    return count

def get_random_word(histogram):
    word_list = []
    for key, value in histogram.iteritems():
        word_list.append(key)
    rand_index = random.randint(0, len(word_list)-1)
    random_word = ''.join(word_list[rand_index])
    return random_word

def my_app(file_name):
    words_list = get_words_list(file_name)
    histogram = create_histogram(words_list)
    # random_word = get_random_word(histogram)
    count = get_count(histogram)
    print count



if __name__ == '__main__':
    file_name = str(sys.argv[1])
    my_app(file_name)
