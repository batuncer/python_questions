# Please take a list of values as input and sort the unique values.
# Sample input: 34, 23, 56, 98, 23, 45, 98, 98, 34, 101, 3
# Sample output: 3, 23, 34, 45, 56, 98, 101


number_list = 34, 23, 56, 98, 23, 45, 98, 98, 34, 101, 3
# we convert it to set because set containes only unique elements
# we want to sort numbers, set doesnt has attribute "sort" for this we convert it to list

new_list=list(set(number_list)) 

print(new_list)