#Dictionaries
user = {'Ancient': 800, 'Thragg': 740, 'Alice': 720}
level_requirnment = [user for user, level in user.items() if level > 500]
print(level_requirnment)

#Lists
players = ['Alice', 'Thragg', 'Ancient']
player_length = [player for player in players if len(player) > 10]
print(player_length)
