"""
Camping List
Daniel Kensington
Add to list of camping supplies
List 'items' defined in Lab3_dkensington_list.py
2/1/2026
"""


from Lab3_dkensington_list import items


new_items: list[str] = [
    "sunscreen",
    "bug spray",
    "pocket knife",
    "chair",
    "map"
]


for i in new_items:
    items.append(i)


if __name__ == "__main__":
    print(f"Updated list in reverse-alphabetical order: {sorted(items, reverse=True)}")