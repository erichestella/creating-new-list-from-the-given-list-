#add title
print('\nCREATE NEW LIST FROM THE GIVEN TWO LIST.\n')

#given list
integer_list1 = [10, 65, 25, 33, 93]
integer_list2 = [40, 45, 60, 75, 90]

#total list of given list
total_list = []

#function for integerlist1 to check if its odd number
for i in integer_list1:
    if (i % 2 != 0): 
        total_list.append(i)

#function for integerlist2 to check if its even number
for i in integer_list2:
    if (i % 2 == 0):
        total_list.append(i) 

print('New List:', total_list)


