import re

# Email Addresses

with open('info.txt', 'r') as data:
  contents = data.read()

result = re.search(r'\w+@\w+.\w+', contents)

print(result.group())
