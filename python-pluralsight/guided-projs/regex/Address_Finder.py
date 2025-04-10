import re

# IP Addresses

with open('info.txt', 'r') as data:
  contents = data.read()

# Pattern currently matches the address in demo, but not any address ever.
result = re.search(r'\d+\s(\w+\s){2}\w+\s#\d+\s\w+\s\w+,\s\w{2}\s\d{5}\s\w{3}', contents)

print(result.group())
