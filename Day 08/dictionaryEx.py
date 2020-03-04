#Indroducing Dictionary

Students={'Ali':18,'Rahim':12,'Karim':22,'Joya':25}
print('All Students : ')
print(Students)
print('Print by key Rahim :')
print(Students['Rahim'])

#Finding all the methods
print(dir(Students))

#Updating Dictionary
print('add Sarah to our existing dictionary')
Students.update({'Sarah':9})
print(Students)
print('if exist update dictionary')
Students.update({'Karim':12})
print(Students)

#Delete Dictionary data
print('Delete by key :')
del Students['Ali']
print(Students)

#Dictionary Items
print('Print Items:')
print('Students Name: %s' % Students.items())
print('Convert dic to list :')
print('Students Name: %s' % list(Students.items()))

#Printing key
print('Print Only Keys :')
for key in Students.keys():
    print(key)

#Printing value
print('Print Only value :')
for values in Students.values():
    print(values)

#Printing key and value
print('Print Keys and Values :')
for key in Students.keys():
    print(key + '=' +str(Students[key]))

#Printing all the items using loop
print("# Loop over items and unpack each item.")
for k,v in Students.items():
    #Display key and value
    print(k,v)
