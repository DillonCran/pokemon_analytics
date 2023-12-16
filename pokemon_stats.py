# script to pull pokemon data into a database

import numpy as np
import pandas as pd

pkmn_df_data = pd.read_csv('pokemon_analytics\data\pokemon_data_1223.csv')
pkmn_df = pd.DataFrame(pkmn_df_data)

print(pkmn_df.head(1).columns['name'])


# func to sort data by pokemon name
def get_pkmn_data(df):
    pkmn_name = input("Enter a pokemon name: ")
    pkmn_data = df.loc[df['Name'] == pkmn_name]
    print(pkmn_data)
    return pkmn_data
    

# file interface
running = True

    








# pulls headers and ! into lists to be added to the database

header_path = 'pokemon_analytics\data\data_headings.txt'
help_pos = 26
help = ""
with open(header_path, 'r') as file:
    for line in file:
        # split line into two strings, one from the 0 position to the 26th, and the other from the 27th to the end
        header = line[:help_pos]
        help = line[help_pos:]
        cleaned_header = header.strip()
