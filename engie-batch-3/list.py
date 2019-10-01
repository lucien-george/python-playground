# -*- coding: utf-8 -*-

beatles = ['paul', 'john', 'ringo']
#print(type(beatles))

#print(beatles[1])
#
#print(beatles[0:2])
#
#print(beatles[-3:-1])
beatles.append('george')
print(len(beatles))
print(beatles)


# for loop instead    
beatles[0] = beatles[0].upper()
beatles[1] = beatles[1].upper()
beatles[2] = beatles[2].upper()
beatles[3] = beatles[3].upper()


print(beatles)
del(beatles[0])

print(beatles)

# CRUD
# Create => list.append(element)
# Read => list[index] / list[start:end]
# Update => list[index] = new_value
# Delete => del(list[index])

for index, beatle in enumerate(beatles):
    print(f"{index + 1}. {beatle}")
    

















