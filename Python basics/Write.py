file = open("test.txt")

file.close()

# opening a file without a need for file.close()
# with open("test.txt", 'r') as file:   # open thw file in read mode by adding 'r'
# with open("test.txt", 'w') as file:   # open thw file in write mode by adding 'w'


# 1- read the file and store all lines in list
# 2- reverse the list
# 3- write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()  # 1
    reversed(content) # 2
    with open('test.txt', 'w') as writer:
       for line in reversed(content):
            writer.write(line)