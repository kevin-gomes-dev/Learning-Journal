result = []

def search(filename, text, text2):
    with open(filename) as f:
        for line in f:
            if text in line and text2 in line:
                print(line)
                #modify the two lines below
                result.append('Day is ' + line.strip().split()[0] +
                             ' The user is  ' + line.strip().split()[12] + 
                             ' and they tried to connect over ' + line.strip().split()[-2])
                print(result)
                
search('Security.log', 'Failed', '2783')
