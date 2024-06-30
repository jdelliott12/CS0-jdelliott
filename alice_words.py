import re

file = open('alice.txt', 'r')
text = file.read().lower()
file.close()

words = re.findall(r'\b[a-z]+\b', text)

counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

file = open('alice_words.txt', 'w')
file.write('Word              Count\n')
file.write('=======================\n')
for word in sorted(counts):
    file.write(f'{word:20} {counts[word]}\n')
file.close()

print('In the book "alice" appears', counts['alice'], 'number of times.')