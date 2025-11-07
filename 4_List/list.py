Student_info = [ "pritam", "24", "Jharsuguda" ]
print("Student details:", Student_info)

# lets modify the name pritam to pritesh

Student_info[0] = "pritesh"
print("Updated student details:", Student_info)

#calculate the length of the list
length = len(Student_info)
print("Length of the list:", length)

# lets access individual elements
name = Student_info[0] 
age = Student_info[1]
city = Student_info[2]
print("Name:", name)
print("Age:", age)
print("City:", city)