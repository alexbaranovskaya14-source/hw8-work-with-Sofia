# part with find() and rfind()
st_1 = 'This string is used to study string methods such as find() and rfind()'
print('First entrance from the left:', st_1.find('string'))
print('First entrance from the right:', st_1.rfind('string'))

# with start parameter
print('First entrance from the left:', st_1.find('s', 4))
print('First entrance from the right:', st_1.rfind('s', 4))

# with start and end parameters
print('First entrance from the left:', st_1.find('find', 30, 70))
print('First entrance from the right:', st_1.rfind('find', 30, 70))


# an example with no such symbol in string
st_2 = 'hello, world'
print(st_2.find('a'))
print(st_2.rfind('a'))

