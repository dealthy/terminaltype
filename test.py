import os
dirpath = os.path.dirname(os.path.realpath(__file__))
print("shuf -n 1 " + str(dirpath)+ "/words.txt")