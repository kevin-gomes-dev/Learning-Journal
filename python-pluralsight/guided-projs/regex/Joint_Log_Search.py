result = []

def search(filename, text, text2):
    with open(filename) as f:
        for line in f:
            if text.lower() in line.lower() and text2.lower() in line.lower():
                print(line)
                result.append(line)

search('Secure.log', 'Failed', 'x')
