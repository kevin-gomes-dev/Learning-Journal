import os

# Returns list of acro,definition pair if found, otherwise False
def find_acro(path,acro):
    with open(path,'r') as file:
        for line in file:
            acro_pair = line.strip().split("-")
            if acro_pair[0].strip().upper() == str(acro.upper()):
                return acro_pair
        return False

# Returns True if added, False if not
def add_acro(path,acro,defi):
    if acro == "" or defi == "":
        return False
    with open(path,'a') as file:
        file.write('\n')
        str_to_write = f'{acro} - {defi}'
        file.write(str_to_write)
        return True

# Returns False if no path given
def acro_program():
    path = input("Enter path including filename: ")
    if not path:
        return False
    while True:
        mode = input("Enter mode. 1 for find, 2 for add: ")
        if mode == "":
            break
        if mode == "1":
            acro = input("Enter acronym: ")
            acro_pair = find_acro(path,acro)
            print(acro_pair) if acro_pair else print(f'The acronym given, {acro}, does not exist.')
        elif mode == "2":
            acro = input("Enter acronym: ")
            defi = input("Enter definition: ")
            status = add_acro(path,acro,defi)
            print(f'Success: {acro} - {defi}') if status else print(f'Fail: {acro} - {defi}')
        else:
            print("Input given doesn't correspond to mode.")
        print()

# Moving a bunch of sub files from various folders into centralized one
def move_subs(path):
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
                print("OLD:",old_path)
                print("NEW:",new_path)
                # Uncomment when ready to rename/move
                # os.rename(old_path,new_path)
                print("Done!")
            except:
                print("Couldn't print int of:",x)
        print("===================================")

# Load any function with params
def main():
    choice = input("Give name of function. If params, separate with ,. Like so - multiply_2,5,6\n")
    fixed_choice = choice.strip().split(',')
    func = fixed_choice[0]
    args = fixed_choice[1:] if len(fixed_choice) > 1 else []
    # Call function with params
    if func in globals():
        globals()[func](*args)
    
    
if __name__ == "__main__":
    main()