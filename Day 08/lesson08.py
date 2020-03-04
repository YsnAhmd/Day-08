#LIst
friends=['Patkhet','Moba','Dadu','Bus Driver']
for x in friends:
    print(x,end=',')

#List length
print('\nList Length:')
print(len(friends))
print('Total number of friends : {0}'.format(len(friends)))

#Finding index
for num,name in enumerate(friends):
    print('Friends {}: {}'.format(num,name))

#Indroducing tuple
print("\nNew List:")
digits=(1,2,3,4,5,6,7,8,9)
print(min(digits))
print(max(digits))
print(sum(digits))