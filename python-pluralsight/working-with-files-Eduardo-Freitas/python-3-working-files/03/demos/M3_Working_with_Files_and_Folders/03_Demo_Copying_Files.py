import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)

def copy_folder(src, dst):
    shutil.copytree(src, dst)

#copy_file('./files/02_file.txt', './files/subfolder')
copy_folder('./files', './files/new_flder')