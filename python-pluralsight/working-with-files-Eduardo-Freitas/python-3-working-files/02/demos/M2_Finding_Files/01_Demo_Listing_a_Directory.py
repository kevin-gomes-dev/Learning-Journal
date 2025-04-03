import os

def list_dir(fld):
    for fn in os.listdir(fld):
        print(fn)

list_dir('./files')