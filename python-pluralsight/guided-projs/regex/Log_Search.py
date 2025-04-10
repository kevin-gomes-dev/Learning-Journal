import re
result = []

def search(filename, text):
    with open(filename) as f:
        for line in f:
            mat = re.search(r'for\snobody',line.lower())
            if mat:
                print(line)
                result.append(line)

search('Secure.log', 'failed')
