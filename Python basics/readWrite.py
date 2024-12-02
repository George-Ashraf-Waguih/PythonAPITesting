file = open('test.txt')
# file.read()     # Read all content of file
# print(file.read())
# print(file.read(5))  # Read first 5 characters
# print(file.readline()) # Read whole line and stops at end
# print(file.readline()) # Read whole next line

# Print line by line
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#Read lines instead of 1 line at a time 
list = file.readlines()
for line in list:
    print(line)

file.close()
