# Contains all our functions we're callling since the module is set up as just a bunch of demos.
import xml.etree.ElementTree as ET
import os, fnmatch, shutil, zipfile, csv,json,pickle,person
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

# If each_line = true, reads each line and returns list of strings
def read_text(file,each_line = False) -> str | list[str]:
    lines = []
    with open(file,'r') as fp:
        if not each_line:
            return fp.read()
        lines = []
        for line in fp.readlines():
            lines.append(line)
            # Unecessary? As the for loop already goes through every line...
            # line = fp.readline()
        return lines
            
# If append = true, add to end of file instead of creating/overwriting
def write_txt(path,output,append = False):
    mode = 'w' if not append else 'a'
    with open(path,mode,encoding='utf-8') as fp:
        fp.write(output)
    
# Changing this completely from the lesson to make it more dynamic and use csv methods
# The first line we return will be the header if we have one, denoted as such.
def read_csv(path: str) -> list[str]:
    # Abort if we didn't pass a csv file. More specific exception class? Or define one?
    if not path.endswith('csv'):
        raise Exception('File is not a CSV file.')
    lines = []
    with open(path) as csv_f:
        # First get our info. Could have combined it all into one line but wanted to show.
        raw_text = csv_f.read()
        # Rewind back to start now that we already have our info for the sniffer
        csv_f.seek(0)
        sniffer = csv.Sniffer()
        sniffed_file = sniffer.sniff(raw_text)
        has_header = sniffer.has_header(raw_text)
        delimiter = sniffed_file.delimiter
        
        rows = csv.reader(csv_f,delimiter=delimiter)
        for row in rows:
            if has_header and rows.line_num == 1:
                lines.append(f'HEADER: {" | ".join(row)}')
            else:
                lines.append(f'{" | ".join(row)}')
    return lines

def write_csv(path,header,row):
    # newline='' not needed? Same output without
    with open(path,'w',newline='') as csv_f:
        # Use quotechar in case data has literal " or whatever char for it
        # Use QUOTE_MINIMAL to minimize quoting in data
        writer = csv.writer(csv_f,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)

# Make more dynamic than lesson by getting all keys and going through them.
# This means we need to keep doing this for however many keys there are for each child.
# But how many children are there? Recursively?
# Using tree metaphor, 1 tree, x branchs, and each branch could have y branches.
# For loop for branches of children (x), then would need another for loop for every branch
# But since every branch of a branch could itself have z branches...recursive
# Apparently these are just nodes?
# Note that tabbing is done regardless of the file's tabbing. We could use tail to respect,
# but since this is parser, we make it a specific format

# tab_enabled chooses whether to tab at all when printing
# Return list of strings to be printed or handled
def parse_xml_et(path,tab_enabled = True) -> list[str]:
    lines = []
    # Our recursive helper func to go through all branches of all branches
    # Can't go infinite unless your file was infinite
    def parse_branch(branch: ET.Element,tab_count = 0,tab_enabled = True,lines = lines):
        # print(f'count: {tab_count}')
        tab = '\t'*tab_count if tab_enabled else ''
        # Now that we've established this branch is an endpoint, handle its data
        keys = branch.keys()
        # print(f'Branch keys: {keys}, branch tail: {repr(branch.tail)}')
        for k in keys:
            # print(f'Data for {branch.tag} (tag): {k} (key) = {branch.attrib[k]} (attrib[k])')
            # print(f'{tab}{k}: {branch.attrib[k]} | tag: {branch.tag}')
            lines.append(f'{tab}{k}: {branch.attrib[k]} | tag: {branch.tag}')
            # For every branch we could have x branches, and so on...
            # So consider a branch as a tree and parse it as if it's the root
            # for b in branch:
            #     print(f'Tag: {b.tag} | Keys: {b.keys()}')
            #     b_keys = b.keys()
            #     for b_key in b_keys:
            #         print(f'\t{b_key} (b_key): {b.attrib[b_key]} (b.attrib[b_key])')
            # For each branch connected to our branch, parse it seperately
        for b in branch:
            # First add a tab because we are in a new branch. Since that's parsed seperately,
            # if the new branch itself has children, it'll come here and +1 without doing -1
            # to ensure correct indentation. Then coming up the stack will do the -1
            # as many times as you had calls to the func. Hard to explain, use debugger to see
            tab_count+=1
            parse_branch(b,tab_count,tab_enabled)
            # Once we're done with the branch, go back to normal indent from previous one.
            tab_count -= 1
    tree = ET.parse(path) # ET.ELementTree[Element[str]]
    root = tree.getroot() # ET.Element[str]
    lines.append(f'Root tag: {root.tag}, root keys: {root.keys()}')
    for branch in root:
        # The first tab_enabled is the parameter, the second is the value
        # gotten from the main func
        parse_branch(branch,tab_enabled = tab_enabled)
    return lines

# Given the element, it's attribute and value, write it to the xml file in path
# Create an element, give it an attribute and assign a value to it, then add that element
# to the root of the tree. You can do a lot with the created element before adding to tree 
def add_xml_element_et(path,ele,attr,value):
    tree = ET.parse(path)
    root = tree.getroot()
    child = ET.Element(ele)
    child.attrib[attr] = value
    child.tail = '\n'
    root.append(child)
    tree.write(path)
    
def change_xml_element_et(path,ele,attr,old_val,new_val):
    tree = ET.parse(path)
    root = tree.getroot()
    # Find by matching element, attribute, and its old value. We need to know its old value?
    # Is there a way to find it just with element and attribute? Could not be unique however...
    # What if you had 2 of the same, but one inside one set of tags and the other in another?
    # How would you change the 2nd compared to the first if ele, attr and val are same?
    # .findall()? Does it go sequentially? .findall()[index]
    child = root.find(f'./{ele}[@{attr}=\'{old_val}\']')
    # Change key attr to be new value.
    child.attrib[attr] = new_val
    tree.write(path)

# The parameter pretty allows us to not have to worry about recursively tabbing things
# Dumps allows us to avoid finding everything
def parse_json(path,pretty: int = None,sort = False):
    with open(path) as json_file:
        data = json.load(json_file)
        dumps = (json.dumps(data,indent=pretty,sort_keys=sort))
    return dumps

# Update the data at item, pos, and key with value. Assumes item is an array
# Changed to allow for non-lists
# It's a bit sloppy...reads, changes the one value you want, then rewrites everything
# Also can't handle inner objects within objects, seems to be base level 1.
# Would require recursion. If what we're looking at is a dict, call again
# Do this until it's not a dict, then change. But what if it's a list?
# Call again and look within to find a base level item?

# So comb through entire structure, deepest, then back one level, next deepest, etc.
# Keep doing until you either find data[key] to exist or return that it doesn't
# If it does, then ask if list or not. If not...I'll do this another time
def update_json(path,item,pos: int = 0,key = None,value = None,log = False,indent = 4):
    if key == None:
        return 'No key given.'
    with open(path) as json_file:
        data = json.load(json_file)
        try:
            is_arr = type(data[item]) == list
        except KeyError as e:
            print(f'Error: no item {item} found in data.')
            raise
        if is_arr:
            # Should be try catch cause it's possible it doesn't exist
            print(f'Updating data item {item} at pos {pos}, key {key}, old value '
                  f'{data[item][pos][key]} to '
                  f'{value}') if log else ...
            data[item][pos][key] = value
        else:
            print(f'Updating data item {item}, key {key}, old value '
                  f'{data[item][key]} to '
                  f'{value}') if log else ...
            data[item][key] = value
    with open(path,'w') as write_file:
        json.dump(data,write_file,indent=indent)
        print("Update complete") if log else ...
        
def serialize(obj):
    pickled = pickle.dumps(obj,protocol=pickle.HIGHEST_PROTOCOL)
    # print(f'Serialized object: \n{pickled}\n')
    return pickled

def deserialize(serial_obj):
    unpickled = pickle.loads(serial_obj)
    # print(f'Deserialized object: \n{unpickled}\n')
    return unpickled

def obj_to_file(path,obj):
    # Other way is to open file and do pickle.dump(obj,protocol)
    obj_bytes = serialize(obj)
    with open(path,'wb') as file:
        file.write(obj_bytes)
    return obj_bytes

# Lesson has obj in the param but immediately changes it in code without using.
def file_to_obj(path):
    with open(path,'rb') as file:
        obj = pickle.load(file)
    return obj

def main():
    # Call whichever function to test. I used dir_roor and the like to stay in the root
    # Completely unnecessary and would be handled somewhere else in actual code
    # Because this would be restructured as multiple modules
    pass
    # dir = input("Enter directory: ")
    # Assuming your cwd contains your exercise files folder...accounts for windows \
    dir_root = os.path.join(os.getcwd(),"python-3-working-files/05/demos").replace('\\','/')
    dir = dir_root + '/files'
    to_zip = [dir + '/subfolder/01_file_test.csv', 
    dir + '/subfolder/01_file_test.txt', 
    dir + '/subfolder/01_test_file.csv', 
    dir + '/subfolder/01_test_file.txt',
    dir + '/01_file_test.csv',
    dir + '/01_file_test.txt']
    to_add = [dir + '/01_file.csv',dir + '/01_file.txt']
    # Make things easy, ftr = Files To Read
    ftr = os.path.join(dir_root,'files_to_read') + '/'
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
    
    # mod 3
    # copy_file(dir + '/02_test.txt',dir + '/testing')
    # copy_dir(dir,dir + '/test')
    # move_files(dir + '/02_test.txt',dir + '/testing/02_test.txt')
    # move_files(dir + '/testing/02_test.txt',dir + '/02_test.txt')
    # move_files(dir,dir_root + '/test')
    # move_files(dir_root + '/test',dir)
    # remove_file(dir + '/02_test.txt')
    
    # mod 4
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
    
    # mod 5
    # print(read_text(ftr + 'backup.py'))
    # print(*read_text(ftr + 'backup.py',True))
    # OR
    # print(''.join([x for x in read_text(ftr+'backup.py',True)]))
    # txt_write = 'This is some text.\nIt has a new line seperator.\nThat\'s all.'
    # write_txt(ftr + 'test_write.txt',txt_write)
    # for i in range(3):
        # write_txt(ftr+'test_write.txt',f'\n-------{i}--------\n'+txt_write,True)
    # print('\n'.join(i for i in read_csv(ftr+'names.csv')))
    # write_csv(ftr+'test_write.csv',['name','age','sex','acct#'],['john','45','M','1234567890'])
    # print('\n'.join(i for i in read_csv(ftr+'test_write.csv')))
    # Create our own xml from base
    # write_txt(ftr+'test.xml',read_text(ftr+'ef_author_mod.xml'))
    # for i in parse_xml_et(ftr+'ef_author_mod.xml'):
        # print(i)
    # add_xml_element_et(ftr+'ef_author_mod.xml','TestTag','TestAttr','TestValue')
    # change_xml_element_et(ftr+'ef_author_mod.xml','domain','name','TypeScript','TS')
    # Create our own json from base
    # write_txt(ftr+"authors_mod.json",read_text(ftr+'authors.json'))
    # parse_json(ftr+'authors.json',4)
    # update_json(ftr+'authors_mod.json','someObj',0,'prop3','val2_mod',True)
    p = person.Person()
    # serial_p = serialize(p)
    # deserial_p = deserialize(serial_p)
    # print(deserial_p.employers)
    # print(obj_to_file(ftr+'bytes_obj.xyz',p))
    # p_from_file = file_to_obj(ftr+'bytes_obj.xyz')
    # print(p_from_file.employers)
    
if __name__ == "__main__":
    main()