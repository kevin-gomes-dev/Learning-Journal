# Contains all our functions we're callling since the module is set up as just a bunch of demos.
import os, fnmatch, shutil, zipfile
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
            print(f'Removing {f}')
            os.remove(f)
        except OSError as e:
            print(f'Error: {f} : {e.strerror}')
    else:
        print(f'Error: {f} is not a file')

def create_zip(zipf, files, option):
    # Create a zip file and call it archive. allowZip64 means allow 64-bit (8byte).
    # zipf is the name of the archive when created. Options are in docs, basically rwx etc
    with zipfile.ZipFile(zipf,option,allowZip64=True) as archive:
        for f in files:
            archive.write(f)

def add_zip(zipf,files,option):
    # Add files to an already existing zip file
    print(f'Is {zipf} a zip? {zipfile.is_zipfile(zipf)}')
    if zipfile.is_zipfile(zipf):
        with zipfile.ZipFile(zipf,option,allowZip64=True) as archive:
            # For each file, check against the entire list of files in zip. If not there, add.
            # Added a bit of caching for performance?
            # After a write, check archive again. If didn't write, archive must be same, no check.
            wrote = False
            lst = archive.namelist()
            for f in files:
                if wrote == True:
                    lst = archive.namelist()
                    wrote = False
                # print(f'Is {f} in list {lst}? {f in lst}')
                if f not in lst:
                    archive.write(f)
                    wrote = True
                else:
                    print(f'File exists in zip {zipf} - {f}')

# Add return type hint for better intellisense
def read_zip(zipf) -> list[zipfile.ZipInfo]:
    files = []
    if zipfile.is_zipfile(zipf):
        with zipfile.ZipFile(zipf,'r',allowZip64=True) as archive:
            for file in archive.namelist():
                files.append(archive.getinfo(file))
    return files
    
# Pass True to "all" to extract all files
def extract_file(zipf,file,path,all = False):
    if zipfile.is_zipfile(zipf):
        with zipfile.ZipFile(zipf) as archive:
            if file in archive.namelist():
                if not all:
                    archive.extract(archive.getinfo(file),path)
                else:
                    archive.extractall(path)

def main():
    # Call whichever function to test
    pass
    # dir = input("Enter directory: ")
    dir_root = "python-3-working-files/04/demos"
    dir = dir_root + '/files'
    to_zip = [dir + '/subfolder/01_file_test.csv', 
    dir + '/subfolder/01_file_test.txt', 
    dir + '/subfolder/01_test_file.csv', 
    dir + '/subfolder/01_test_file.txt',
    dir + '/01_file_test.csv',
    dir + '/01_file_test.txt']
    to_add = [dir + '/01_file.csv',dir + '/01_file.txt']
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
    # remove_file(dir + '/02_test.txt')
    
    # create_zip(dir_root + '/test_add_zip.zip',to_zip,'w')
    # add_zip(dir_root + '/test_add_zip.zip',to_add,'a')
    # zip_lst = read_zip(dir_root + '/test_add_zip.zip')
    # for i in zip_lst:
        # print(f'{i.file_size} actual bytes | {i.compress_size} compressed bytes')
    # extract_file(dir_root + '/test_add_zip.zip',
    #              dir + '/01_file_test.csv',
    #              dir + '/testing/01_file_test.csv',
    #              all = True)
    # remove_file(dir_root + '/test_add_zip.zip')

if __name__ == "__main__":
    main()