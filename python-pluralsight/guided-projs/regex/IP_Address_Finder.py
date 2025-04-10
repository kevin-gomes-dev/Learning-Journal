import re

# IP Addresses

with open('info.txt', 'r') as data:
  contents = data.read()

result = re.search(r'(\d+.){3}\d+', contents)

print(result.group())
