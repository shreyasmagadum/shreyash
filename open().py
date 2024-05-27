file = open('sample.txt', 'w')
file.write('Hello, World!\n')
file.write('This is a new line.')
file.close()

with open('sample.txt', 'w') as file:
    file.write('with Hello, World!\n')
    file.write('with This is a new line.')