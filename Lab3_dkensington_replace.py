"""
Camping List
Daniel Kensington
Replace elements in list of camping supplies
List 'items' defined in Lab3_dkensington_list.py and\
imported from Lab3_dkensington_list.py
2/1/2026
"""


from Lab3_dkensington_add import items
from random import randint


items[randint(1, len(items)-2)] = "binoculars"