import zipfile

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for l in lst:
            zfinf = archive.getinfo(l)
            print(f'{l} => {zfinf.file_size} bytes, {zfinf.compress_size} compressed')

read_zip('./files.zip')