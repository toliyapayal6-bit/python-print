# List : [],chang,indexing,duplicate

a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
print(a1)

#type
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
print(type(a1))

#append
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.append('dhara')
print(a1)

#pop()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.pop()
print(a1)

a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.pop(3)
print(a1)

# clear()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.clear()
print(a1)

# copy()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a2 = a1.copy()
print(a2)

# remove()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.remove('meet')
print(a1)

# sort()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.sort()
print(a1)

# reverse()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.reverse()
print(a1)

#insert()
a1 =['meet','radhvi','dev','raj','manan','bela','meet']
a1.insert(3,'jeel')
print(a1)

a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a1.insert(4,"dev")
print(a1)

# index()
a1 =['meet','radhvi','dev','raj','manan','bela','meet']
a = a1.index("bela")
print(a)
a2 = a1.index("meet")
print(a2)

# count()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
a = a1.count("dev")
print(a)

a1 = ['meet','radhvi','dev','raj','manan','bela','meet','meet']
a2 = a1.count('meet')
print(a2)

# len()
a1 = ['meet','radhvi','dev','raj','manan','bela','meet']
print(len(a1))



# list - int value

a = [1,5,7,4,15,4,2,10]
print(a)

# type()
a =  [1,5,7,4,15,4,2,10]
print(type(a))

# append()
a =  [1,5,7,4,15,4,2,10]
a.append(25)
print(a)

# pop()
a =  [1,5,7,4,15,4,2,10]
a.pop()
print(a)

# clear()
a =  [1,5,7,4,15,4,2,10]
a.clear()
print(a)

# copy()
a = [1,5,7,4,15,4,2,10]
b = a.copy()
print(b)

# remove()
a = [1,5,7,4,15,4,2,10]
a.remove(4)
print(a)

# sort()
a =  [1,5,7,4,15,4,2,10]
a.sort()
print(a)

# reverse()
a =  [1,5,7,4,15,4,2,10]
a.reverse()
print(a)

# insert()
a =  [1,5,7,4,15,4,2,10]
a.insert(2, 9)
print(a)

# index()
a =  [1,5,7,4,15,4,2,10]
b = a.index(4)
print(b)
a1 = a.index(1)
print(a1)

# count()
a = [1,5,7,4,15,4,2,10]
b = a.count(15)
print(b)

a1 = a.count(4)
print(a1)

# len()
a =  [1,5,7,4,15,4,2,10]
print(len(a))



# tuple : (), no chang, indexing,duplicate 

#  tuple - str value

a1 = ('meet','radhvi','dev','raj','manan','bela','meet')
print(a1)

# type
a1 = ('meet','radhvi','dev','raj','manan','bela','meet')
print(type(a1))

# index()
a1 = ('meet','radhvi','dev','raj','manan','bela','meet')
a = a1.index("meet")
print(a)

b = a1.index('raj')
print(b)

# count()
a1 = ('meet','radhvi','dev','raj','manan','bela','meet')
a = a1.count('dev')
print(a)

b = a1.count("meet")
print(b)


# tuple int-value

a = (1,5,7,4,15,4,2,10)
print(a)

a = (1,5,7,4,15,4,2,10)
print(type(a))

# index()
a = (1,5,7,4,15,4,2,10)
b = a.index(4)
print(b)

a1 = a.index(10)
print(a1)

# count()
a = (1,5,7,4,15,4,2,10)
a1 = a.count(4)
print(a1)

b = a.count(10)
print(b)