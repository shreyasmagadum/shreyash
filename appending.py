#Reading Entire File:
file = open('sample.txt', 'r')
content = file.read()
print(content)
file.close()

print()

#Reading Line by Line:
file = open('sample.txt', 'r')
for line in file:
    print(line.strip())
    print()# strip() removes trailing newline characters
file.close()

#using with
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)