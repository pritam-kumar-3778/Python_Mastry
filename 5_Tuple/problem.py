# WAP to count the number of students with the "A" grade in the following tuple.
# ("c", "d", "a", "a", "b", "b", "a")

grades = ("c", "d", "a", "a", "b", "b", "a")

# Using count() method to count occurrences of "a"
a_count = grades.count("a")
print("Number of students with 'A' grade:", a_count)

# Q : Store the above values in a list & sort them from "a" to "d".
grades_list = list(grades)
grades_list.sort()
print("Sorted grades from 'a' to 'd':", grades_list)

