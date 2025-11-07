marks = [96, 65, 78, 84, 60]

#print first two elements
first_two = marks[ :2] #same as marks[0:2]
print("First two marks:", first_two)

#print elements from index 2 to 4 (4 not included)
middle_marks = marks[2:4]
print("Marks from index 2 to 4:", middle_marks)

#negetive indexing
#print last two elements
last_two = marks[-2: ]
print("Last two marks:", last_two)

#print 78 and 84
specific_marks = marks[-3:-1]
print("Specific marks (78 and 84):", specific_marks)

