# Adam E. Farence
# October 29, 2020
# Homework 2, Part 2

# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order

countries = [ "Nigeria", "France","Canada","Egypt","Mexico","Russia","China" ]

# 2) Using a for loop, print each element of the list

for country in countries:
    print(country)

# 3) Sort the list permanently.

alpha_sorted_countries = sorted(countries)
print(alpha_sorted_countries)

# 4) Display the first element of the list.

print("This is the first country in the sorted list:", alpha_sorted_countries[0])

# 5) Display the second-to-last element of the list.

print("This is the second-to-last country in the sorted list:", alpha_sorted_countries[-2])

# 6) Delete one of the countries from the list using its name.

revised_alpha_sorted_countries = alpha_sorted_countries

if "Mexico" in revised_alpha_sorted_countries:
    revised_alpha_sorted_countries.remove("Mexico")
    print("The same list, but with Mexico removed using it's own name:", revised_alpha_sorted_countries)

# 7) Using a for loop, print each country's name in all caps.

all_caps_list = alpha_sorted_countries

for cap_country in all_caps_list:
    print(cap_country.upper())

# PART TWO: Dictionaries

# These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing 
# in *coordinates of CITYNAME*. You can also use https://itouchmap.com/?r=latlong (Links to an external site.).

# Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. 
# If the longitude is W, make it negative. (See here for 
# explanation: https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8 (Links to an external site.))

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. 
# Pick a tree from: https://en.wikipedia.org/wiki/List_of_trees

tree = {
    'name':'Silver fern',
    'species':'A. dealbata',
    'age': 1800000,
    'location_name':'New Zealand',
    'latitude':-40.9006,
    'longitude':174.8860
}

# 2) Print the sentence "{name} is a {years} year old tree that is in {location_name}"

print(f"{tree['name']} is a {tree['age']:,} year old tree that is in {tree['location_name']}")


# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. 
# Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. 
# If it isn't, print "The tree {name} in {location} is north of NYC"


nyc_cords = {
    'latitude':40.7128,
    'longitude':74.0059
}

if tree['latitude'] > nyc_cords['latitude']:
    print(f"The tree {tree['name']} in {tree['location_name']} is North of NYC.")
else:
    print(f"The tree {tree['name']} in {tree['location_name']} is South of NYC.")


# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}."
# If they are younger than the tree, display "{name} was {XXX} years old when you were born."

#user_age = int(input('How old are you?'))
#user_name = input('What is your name?')

# test_user_name = 'Adam'

# test_user_age = 27

# if user_age > tree['age']:
#     age_difference = user_age - tree['age']
#     print(f"You are older than the tree {tree['name']} by {age_difference}.")
# elif user_age < tree['age']:
#     age_difference = tree['age'] - user_age
#     print(f"{tree['name']} was {age_difference:,} years old when you were born.")
# else:
#     print("You are the same age as the tree...somehow.")


# PART TWO: Lists of dictionaries

# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, 
# and (5) Santiago. Each dictionary should include each city's name and latitude/longitude (see note above).

Moscow = {
    'city_name':'Moscow',
    'latitude':55.7558,
    'longitude':37.6173
}

Tehran = {
    'city_name':'Tehran',
    'latitude':35.6892,
    'longitude':51.3890
}

Falkland_Islands = {
    'city_name':'Falkland Islands',
    'latitude':-51.7963,
    'longitude':-59.5236
}

Seoul = {
    'city_name':'Seoul',
    'latitude':37.5665,
    'longitude':126.9780
}

Santiago = {
    'city_name':'Santiago',
    'latitude':-33.4489,
    'longitude':-70.6693
}

world_cities = [
    Moscow,
    Tehran,
    Falkland_Islands,
    Seoul,
    Santiago
]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? 
# Think hard about the latitude.). When you get to the Falkland Islands, also display the message 
# "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.

for city in world_cities:
    if 0 < city['latitude']:
        print(f"The city of {city['city_name']} is above the equator.")
    elif city['city_name'] == 'Falkland Islands':
        print(f"The {city['city_name']} are a biogeographical part of the mild Antartic zone.")

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.

for other_city in world_cities:
    if tree['latitude'] < other_city['latitude']:
        print(f"The city of {other_city['city_name']} is North of the {tree['name']} in {tree['location_name']}.")
    else:
        print(f"The city of {other_city['city_name']} is South of the {tree['name']} in {tree['location_name']}.")

