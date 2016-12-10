import random
import time
import sys
from histogram import get_words_list
from histogram import create_histogram

def my_app(file_name):
    words_list = get_words_list(file_name)
    histogram = create_histogram(words_list)
    print histogram



if __name__ == '__main__':
    file_name = str(sys.argv[1])
    my_app(file_name)
