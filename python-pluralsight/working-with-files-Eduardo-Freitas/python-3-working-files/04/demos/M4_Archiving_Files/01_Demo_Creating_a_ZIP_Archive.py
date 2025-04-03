import zipfile

to_zip = ['./files/subfolder/01_file_test.csv', 
    './files/subfolder/01_file_test.txt', 
    './files/subfolder/01_test_file.csv', 
    './files/subfolder/01_test_file.txt',
    './files/01_file_test.csv',
    './files/01_file_test.txt']

def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)

create_zip('./files.zip', to_zip, 'w')