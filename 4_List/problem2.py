# WAP to check if a list contains  palindrome of elements.
# Hint : use copy() method.
# A palindrome is a sequence that reads the same backward as forward. eg : madam
# [1,2,3,2,1] -> palindrome
# [1,2,3,4,5] -> not a palindrome
# [1, "abc", "abc", 1] -> palindrome

# [1,2,3,2,1] -> If we reverse it we get the same list [1,2,3,2,1], so it is a palindrome.

#Create a list with palindrome elements
list1 = [1,2,3,2,1]

#Create a list with non-palindrome elements
list2 = [1,2,3,4,5]

list1_copy = list1.copy()
list1_copy.reverse()

if (list1 == list1_copy):
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")
