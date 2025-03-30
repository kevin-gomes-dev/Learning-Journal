import os


def find_acro(acro):
    with open('test.txt','r') as file:
        found = False
        for line in file:
            acro_pair = line.split("-")
            if acro_pair[0].strip().upper() == str(acro.upper()):
                found = True
                print(acro_pair[1].strip())
                break
    if not found:
        print(f'The acronym given, {acro}, does not exist.')

def add_acro(acro,defi):
    if acro == "" or defi == "":
        print("Either acronym or definition was blank.")
        return
    with open('test.txt','a+') as file:
        file.write('\n')
        str_to_write = f'{acro} - {defi}'
        file.write(str_to_write)
    print(f'Successfully wrote acronym {acro} and definition {defi}')
    
def main():
    while True:
        inp = input("Enter mode. 1 for find, 2 for add: ")
        if inp == "":
            break
        if inp == "1":
            acro = input("Enter acronym: ")
            find_acro(acro)
        elif inp == "2":
            acro = input("Enter acronym: ")
            defi = input("Enter definition: ")
            add_acro(acro,defi)
        else:
            print("Input given doesn't correspond to mode.")
        print()

# if __name__ == "__main__":
#     main()
path = r'C:\Users\Kevin\Desktop\stuff\MN\subs'
path = os.path.normpath(os.path.realpath(path))

dirs = os.walk(path)
for i,j,k in dirs:
    # Get S/E
    p = i.split('S')
    for x in p:
        try:
            num = int(x[3:5])
            new_name = str(num).zfill(2) + "_eng.ass"
            old_path = i + "\\track4_eng.ass"
            new_path = i + "\\" + new_name
            # old_path = ""
            # new_path = ""
            print("OLD:",old_path)
            print("NEW:",new_path)
            os.rename(old_path,new_path)
            print("Done!")
        except:
            print("Couldn't print int of:",x)
    print("===================================")