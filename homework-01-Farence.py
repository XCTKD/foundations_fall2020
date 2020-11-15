## Adam Ellsworth Farence ##
## 10.27.2020 ##
## Homework 1 ##

## Starting values ##

user_year_of_birth = int(input("In what year were you born?"))
current_date = 2020
if user_year_of_birth > current_date:
    int(input("This isn't Back to the Future. Your real age this time, please"))
## user_age = 27

## user_year_of_birth = current_date - user_age
user_age = current_date - user_year_of_birth

## Output values ##

minutes_a_year = 525600

average_human_heartbeat_per_minute = 80

average_bw_heartbeat_per_minute = 6

average_rabbit_heartbeat_per_minute = 170

## Heartbeat logic ##

user_heart_beat_number = user_age * minutes_a_year * average_human_heartbeat_per_minute

blue_whale_heart_beat_number = user_age * minutes_a_year * average_bw_heartbeat_per_minute

rabbit_heart_beat_number = user_age * minutes_a_year * average_rabbit_heartbeat_per_minute
if rabbit_heart_beat_number > 1000000:
    rabbit_number_string = str(rabbit_heart_beat_number)
    formatted_rabbit_number = (rabbit_number_string[0:3])

else:
    rabbit_heart_beat_number = formatted_rabbit_number

## Print year and heartbeat ##

print("You were born in the year", user_year_of_birth, " Your heart has beaten about", user_heart_beat_number, 
"times. A blue whale's heart on average has beaten", blue_whale_heart_beat_number, 
" times. And a rabbit's heart has beaten on average ", formatted_rabbit_number, "million times.")

## Planetary Logic ##

venus_year = .06152 ## earth years
neptune_year = 165 ## earth years

user_age_in_venus_years = round(user_age / venus_year,2)

user_age_in_neptune_years = round(user_age / neptune_year,2)

## Print planetary years ##

print("You are", user_age_in_venus_years, "years old on Venus.",
"You are", user_age_in_neptune_years, "years old on Neptune.")

## Age comparision logic ##

adams_age = 27

if user_age == adams_age:
    print("You are the same age as Adam")
elif user_age > adams_age:
    age_difference = user_age - adams_age
    print("You are", age_difference, "years older than Adam.")
elif user_age < adams_age:
    age_difference = adams_age - user_age
    print("You are", age_difference, "years younger than Adam.")

## Born in an even or odd year? ##

if user_year_of_birth % 2 == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

## Presidential Stuff ##

Eisenhower = ("Dwight D. Eisenhower", "R", 1960, 1961)
Kennedy = ("John F. Kennedy", "D", 1961, 1963)
Johnson = ("Lyndon B. Johnson", "D", 1963, 1969)
Nixon = ("Richard Nixon", "R", 1969, 1974)
Ford = ("Gerald Ford", "R", 1974, 1977)
Carter = ("Jimmy Carter", "D", 1977, 1981)
Reagan = ("Ronald Regan", "R", 1981, 1989)
BushSr = ("George H.W. Bush", "R", 1989, 1993)
Clinton = ("Bill Clinton", "D", 1993, 2001)
BushJr = ("George W. Bush", "R", 2001, 2009)
Obama = ("Barack Obama", "D", 2009, 2017)
Trump = ("Donald Trump", "R", 2017, 9999)

Presidents = (Eisenhower, Kennedy, Johnson, Nixon, Ford, Carter, Reagan, BushSr, Clinton, BushJr, Obama, Trump)

##  Birth President ##

for president in Presidents:
    currentPres = president
    if user_year_of_birth >= currentPres[2] and user_year_of_birth <= currentPres[3]:
        print(currentPres[0], "was president the same year you were born.")

## Democratic Presidents ##
democratic_president_counter = 0
for president in Presidents:
    current_Dem_Pres = president
    if user_year_of_birth <= current_Dem_Pres[2] and "D" in current_Dem_Pres:
        democratic_president_counter = democratic_president_counter + 1
print("There have been", democratic_president_counter, "Democratic US Presidents since you were born.")