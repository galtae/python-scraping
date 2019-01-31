favorite_colors = ['red', 'pink', 'brown', 'white']

#Create(생성), Read(읽기), Update(갱신), Delete(삭제)

#c
favorite_colors.append('black')
print(favorite_colors)

#r
favorite_colors.insert(3, 'yellow')
print(favorite_colors)

#u
favorite_colors[2] = '갈색'
print(favorite_colors)

#d
favorite_colors.remove('갈색')
print(favorite_colors)

size = len(favorite_colors)
print(size)

del favorite_colors[1]
print(favorite_colors)

size = len(favorite_colors)
print(size)

for i in favorite_colors:
    print (i)