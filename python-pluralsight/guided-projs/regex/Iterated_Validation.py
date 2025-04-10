import re
import sys

test = input('Password? ')

# Must be 8-12 character

if 8 <= len(test) <=12:
  print('Passed length check')
else:
  print('Failed length check')
  sys.exit()

# It must include at least lowercase character [A-Z] 

for char in test:
  k = char.islower()
  if k == True:
    print('passed lowercase check')
    break
if k != 1:
  print('failed lowercase check')
  sys.exit()

# It must included at least one digit [0-9]

for char in test:
  d = char.isdigit()
  if d == True:
    print('passed digit check')
    break
if d != 1:
  print('failed digit check')
  sys.exit()

# It must include at least one Uppercase Character

for char in test:
  u = char.isupper()
  if u == True:
    print('passed uppercase check \n' + test + ' Is a strong password')
    break
if u != 1:
  print('failed uppercase check')
  sys.exit()
