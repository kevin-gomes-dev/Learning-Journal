import os
from datetime import datetime

def get_date(timestmp):
    return datetime.utcfromtimestamp(timestmp).strftime('%d %b %Y')

def get_file_attrs(fld):
    with os.scandir(fld) as dir:
        for f in dir:
            if f.is_file():
                inf = f.stat()
                print(f'Modified {get_date(inf.st_mtime)} {f.name}')

get_file_attrs('./files/subfolder')