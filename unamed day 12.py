import os

if os.path.exists('levels.txt'):
  with open ('levels.txt', 'r') as file:
    result = file.readlines()
    for line in result:
      print(line.strip())

else:
  with open ('levels.txt', 'w') as file:
    file.write('Ancient: 800\n')
    file.write('Thragg: 840\n')
    file.write('Alice: 800\n')

  with open('levels.txt', 'r') as file:
    result = file.readlines()
    for line in result:
      print(line.strip())
