values = [1, 2, "George", 4, 5]
print(values[2])
print(values[-1])
print(values[:-1])

values.insert(3, "Ash")
print(values)
values.append("Wag")
print(values)

values[2]='GEORGE'
print(values)

del values[0]
print(values)

print('==================================')

val = (1, 2, 'Geo', 4.5)
print(val[1])
print('==================================')

dic = {'a':2, 4:'bcd', 'c':'Hello world'}
print(dic[4])
print(dic['c'])

#
dict = {}
dict['firstname'] = "Geo"
dict['lastname'] = "Ash"
dict['gender'] = "Male"
print(dict)
print(dict["lastname"])