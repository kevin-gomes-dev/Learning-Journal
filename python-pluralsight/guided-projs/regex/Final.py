import re

# regexs
phone = r'((\d{3}-){2}\d{4})'
email = r'\w+@\S+\.\S+'
ip = r'((\d{1,3}\.){3}\d{1,3})'
# Getting the contents of the file
textfile = open('Final_Search.log', 'r')
filetext = textfile.read()
textfile.close()

# Getting IP Addresses

IP_Address = [i[0] for i in re.findall(ip,filetext)]
print(IP_Address)

# Getting Email Addresses

Email_Address = re.findall(email, filetext)
print(Email_Address)

# Getting Phone Numbers

Phone_Numbers = [i[0] for i in re.findall(phone,filetext)]
print(Phone_Numbers)
