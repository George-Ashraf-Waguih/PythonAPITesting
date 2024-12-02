str = "GeorgeAshraf.com"

str1 = " is the best"

str2 = "GeorgeAshraf"

print(str[1])
print(str[0:6])
print(str+str1)

print(str2 in str)  # sub string check
strList = str.split(".")
print(strList)
print(strList[0])

str3 = " great "
print(str3.strip())
print(str3.lstrip())
print(str3.rstrip())