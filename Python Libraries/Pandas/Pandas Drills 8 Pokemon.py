import numpy as np
import pandas as pd
pokemon = pd.DataFrame({'evolution':['Ivysaur','Charmeleon','Wartortle','Metapod'], 'hp':[45,39,44,45], 'name':['Bulbasaur','Charmander','Squirtle','Caterpie'] , 'pokedex':['yes','no','yes','no'],'type':['grass', 'fire', 'water', 'bug']})
print(pokemon)

#  Oops...it seems the DataFrame columns are in alphabetical order. Place the order of the columns as name, type, hp, evolution, pokedex
#pokemon= pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']] # this works but just below is a solution that also work for new names!!!!!!!!!!!!!!
pokemon.columns = ['name', 'type', 'hp', 'evolution', 'pokedex']
print( "\n Place the order of the columns as name, type, hp, evolution, pokedex: \n", pokemon)

# Add another column called place, and insert what you have in mind # I added 2 ;-)
pokemon['New column'] = [1,2,3,4]
print("\n Add new column via pokemon['New column'] = [1,2,3,4] : \n",pokemon)
pokemon.insert(2,'2nd New column', ['Add','a','second','column'])
print("\n Add new column via pokemon.insert : \n", pokemon)

#  Present the type of each column
print("\n columns dtypes : \n", pokemon.dtypes)

