import os
from pathlib import Path

def rename_file_1(src, dst):
    os.rename(src, dst)

def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)

#rename_file_1('./files/text.txt', './files/test.txt')
rename_file_1('./files/test.txt', './files/text.txt')