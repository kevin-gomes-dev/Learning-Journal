def read_txt(fn):
    with open(fn) as f:
        print(f.read())

def read_txt_by_line(fn):
    with open(fn) as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()

def write_new_txt(fn, str):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(str)

def append_line_txt(fn, str):
    with open(fn, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(str)

#read_txt('./files_to_read/backup.py')
#read_txt_by_line('./files_to_read/backup.py')
#write_new_txt('./files_to_read/example.txt', 'this is a test...')
append_line_txt('./files_to_read/example.txt', 'this is an extra line')
