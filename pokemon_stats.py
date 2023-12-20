# script to pull pokemon data into a database

# imports
from config import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
# Thank god theres a library for this
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity
from pokemontcgsdk import RestClient # pokemonTCG api tookin

# find card by id
card = Card.find('xy1-1')
# find card by parameters
cards = Card.where(q='set.name:generations supertype:pokemon')
# find all cards
cards = Card.all()
# Get all cards, but only a specific page of data
cards = Card.where(page=5, pageSize=250)
# find set by code
set = Set.find('base1')
# filter sets by parameters
sets = Set.where(q='legalities.standard:legal')
# Get all Sets
sets = Set.all()
# Get all Types
types = Type.all()
# Get all Subtypes
subtypes = Subtype.all()
# Get all Supertypes
supertypes = Supertype.all()
# Get all Rarities
rarities = Rarity.all()


# pokemonTCG api tookin\
RestClient.configure(TOKEN)