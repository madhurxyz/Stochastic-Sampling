import random
import time
import sys

def my_app(file_name):
    print file_name
    return file_name



if __name__ == '__main__':
    file_name = str(sys.argv[1])
    my_app(file_name)
