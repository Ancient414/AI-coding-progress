with open('player_levels.txt', 'w') as file:
  file.write('Ancient: 840\n')
  file.write('Thragg : 800\n')
  file.write('Alice : 1\n')

with open('player_levels.txt', 'r') as file: 
  content = file.readlines()
  for line in content:
    print(line.strip())
