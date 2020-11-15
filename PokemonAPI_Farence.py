## Adam E. Farence ##
## 11.03.2020 ##
## Pokemon API ##
import requests

# What is the URL to the documentation?

#### The documentation URL is: https://pokeapi.co/docs/v2

# What pokemon has the ID of 55?

print("Hello")
url = "https://pokeapi.co/api/v2/pokemon/55"
response = requests.get(url, allow_redirects=True)
data = response.json()
print(data['name'])
print(response)

# How tall is that pokemon?

print(data['height'])

print('----')

# How many versions of Pokemon games have been released?

url = "https://pokeapi.co/api/v2/version"
response2 = requests.get(url, allow_redirects=True)
data = response2.json()
print(data['count'])
print(response2)


# Print out the name of every electric-type pokemon.

url = "https://pokeapi.co/api/v2/type/electric"
response3 = requests.get(url, allow_redirects=True)
data = response3.json()
layer1 = data['pokemon']
layer_counter = 0
for electric_pokemon in response3:
    print(layer1[layer_counter]['pokemon']['name'])
    layer_counter = layer_counter + 1
    print('----')



# What are electric-type Pokemon called in the Korean version of the game?

url = "https://pokeapi.co/api/v2/language/ko/"
response4 = requests.get(url, allow_redirects=True)
data = response4.json()
layer1 = data['names']
print(layer1)

# Who has a higher speed stat, Eevee or Pikachu?

url = "https://pokeapi.co/api/v2/pokemon/25"
response = requests.get(url, allow_redirects=True)
data = response.json()
layer1 = data['stats']
print(layer1[0])