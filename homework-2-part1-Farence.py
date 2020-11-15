import statistics

# Adam E. Farence 
# October 29th, 2020
# Homework 2, Part 1

## LISTS!

list1 = [22, 90, 0, -10, 3, 22, 48]

sorted_list = sorted(list1)

# Prints number of elements in the list
print("This is the number of elements in the list", len(list1))

# Prints 4th element in the list

print("This is the 4th element in the unsorted list:", list1[3])

# Sum of the 2nd and 4th element of the list

sum_of_second_and_fourth_element = list1[1] + list1[3]
print("This is the sum of the 2nd and 4th element in the list:", sum_of_second_and_fourth_element)

# Display the 2nd-largest value in the list.

print("This is the second largest value in the list:", sorted_list[1])

# Display the last element of the original unsorted list

print("This is the last element of the unsorted list:", list1[-1])

# Display the sum of all of the numbers divided by two.

sum_numbers_div2 = sum(list1)/2
print("This is the sum of all numbers divided by two.", sum_numbers_div2)

# Print whether the median or the mean of the numbers is higher
print(sorted_list)

median_list_number = statistics.median(sorted_list)

mean_list_number = statistics.mean(sorted_list)

if median_list_number > mean_list_number:
    print("The median is larger:", median_list_number)
elif median_list_number < mean_list_number:
    print("The mean is larger:", mean_list_number)
elif median_list_number == mean_list_number:
    print("The median and mean of this list are the same:", median_list_number)

## DICTIONARIES!

## Movie stuff
movie = {
    'title':'Deadpool',
    'year':'2016',
    'director':'Tim Miller'
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie["budget"] = 58000000
movie["revenu"] = 7826000000

if "budget" > "revenu":
    print("That was a bad investment.")
elif (5 * "budget") < "revenu":
    print("That was a great investment.")
else:
    print("That was an okay investment.")

## NYC Borough Population

NYC_borough_population = {
    'Manhattan':1600000,
    'Brooklyn':2600000,
    'Bronx':1400000,
    'Queens':2300000,
    'Staten Island':470000
}

print_this_value = NYC_borough_population['Brooklyn']
print(f'The population of Brooklyn is: {print_this_value:,}')

# Population of all 5 boroughs

pop_sum = sum(NYC_borough_population.values()) 

print(f'The population accross all five boroughs is: {pop_sum:,}')

# Percentage of NYC's population living in Manhattan.

percent_living_in_manhattan = NYC_borough_population['Manhattan'] / pop_sum

print("The percentage of New Yorkers living in Manhattan is:", "{:.2%}".format(percent_living_in_manhattan))
