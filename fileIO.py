
import os, sys, time


path = 'C:\\A\\'
time = os.path.getmtime("C:\\A\\")


def read_text_file():
    with open("C:\\A\\", 'r') as f:
        print(f.read())

for file in os.listdir():
    if file.endswith(".txt"):
        print (read_text_file, time)

