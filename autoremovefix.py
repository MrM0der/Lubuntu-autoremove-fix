import os
f = open('message.txt', 'r')
text = f.read()
f.close()

plist = text.split()

for i in plist:
    print(i)
    os.system(f'sudo apt-mark manual {i}')
