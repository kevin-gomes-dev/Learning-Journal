from pathlib import Path

def glob_match(fld, search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)

#glob_match('./files', '*2*.t*')
glob_match('./files/subfolder', '*1_t*file_*c*.t*')