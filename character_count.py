message = 'All this Brexit stuff is a nightmare.'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
