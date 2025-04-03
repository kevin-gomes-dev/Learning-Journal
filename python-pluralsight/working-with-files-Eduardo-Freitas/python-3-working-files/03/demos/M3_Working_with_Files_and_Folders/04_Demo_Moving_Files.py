import shutil

def move_files(src, dst):
    shutil.move(src, dst)

#mv_files('./files/text.txt', './files/subfolder/text.txt')
#mv_files('./files', './xyz')
#mv_files('./xyz', './files')