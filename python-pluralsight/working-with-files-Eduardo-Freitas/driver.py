# Contains all our functions we're callling since the module is set up as just a bunch of demos.
import os, fnmatch, shutil
from pathlib import Path
from datetime import datetime

def list_dir(dir: str = "./"):
    for file_name in os.listdir(dir):
        print(file_name)

def ends_with(dir: str = "./",cri: str = ""):
    file_list = [] # Append files that end with criteria
    for fn in os.listdir(dir):
        if fn.endswith(cri):
            file_list.append(fn)
    return file_list

def starts_with(dir: str = "./",cri: str = ""):
    file_list = [] # Append files that end with criteria
    for fn in os.listdir(dir):
        if fn.startswith(cri):
            file_list.append(fn)
    return file_list

def match(dir,cri):
    file_list = []
    for fn in os.listdir(dir):
        if fnmatch.fnmatch(fn,cri):
            file_list.append(fn)
    return file_list

# Difference from match is we don't list dir contents and then loop through.
# We instead apply glob to the path itself
def match_glob(dir,cri):
    file_list = []
    path = Path(dir)
    for n in path.glob(cri):
        file_list.append(n)
    return file_list

# Change to use non-deprecated function
def get_date(timestamp: float):
    # return datetime.utcfromtimestamp(timestamp).strftime('%d %b %Y')
    return datetime.fromtimestamp(timestamp).strftime('%d %b %Y %H:%M:%S')

def get_file_attr(dir: str):
    file_list = []
    modified_list = []
    access_list = []
    with os.scandir(dir) as sc_dir:
        for dir_entry in sc_dir:
            if dir_entry.is_file():
                attributes = dir_entry.stat()
                file_list.append(dir_entry.name)
                modified_list.append(f'Modified on {get_date(attributes.st_mtime)}')
                access_list.append(f'Accessed on {get_date(attributes.st_atime)}')
    return [file_list,modified_list,access_list]

# Careful with shutil and moving/copying/deleting!
def copy_file(src,dest):
    shutil.copy(src,dest)

def copy_dir(src,dest):
    shutil.copytree(src,dest)
    
# Can do either one file or entire directory, as move is recursive
def move_files(src,dest):
    print(f'src: {src}, dest: {dest}')
    shutil.move(src,dest)

def rename_file_1(src,dest):
    os.rename(src,dest)

def rename_file_2(src,dest):
    f = Path(src)
    f.rename(dest)
    
def remove_file(f):
    if os.path.isfile(f):
        try:
            print(f'Removing {f}...')
            os.remove(f)
        except OSError as e:
            print(f'Error: {f} : {e.strerror}')
    else:
        print(f'Error: {f} is not a file')

def main():
    # Call whichever function to test
    pass
    # dir = input("Enter directory: ")
    dir_root = "./python-3-working-files/03/demos"
    dir = dir_root + '/files'
    # list_dir(dir)
    # print(ends_with(dir,"txt"))
    # print(starts_with(dir,"01"))
    # print(match(dir,"*.csv"))
    # print(match(dir,"*2_*_*.*"))
    # print(match_glob(dir,"*2*.t*"))
    # [[file1,file2,...],[mod1,mod2,...][acc1,acc2,...]]
    # info_list = get_file_attr(dir)
    # for i in range(len(info_list[0])):
        # print(info_list[0][i],info_list[1][i],info_list[2][i],sep = " | ")
    # copy_file(dir + '/02_test.txt',dir + '/testing')
    # copy_dir(dir,dir + '/test')
    # move_files(dir + '/02_test.txt',dir + '/testing/02_test.txt')
    # move_files(dir + '/testing/02_test.txt',dir + '/02_test.txt')
    # move_files(dir,dir_root + '/test')
    # move_files(dir_root + '/test',dir)
    remove_file(dir + '/02_test.txt')

if __name__ == "__main__":
    main()