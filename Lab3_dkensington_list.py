"""
Camping List
Daniel Kensington
List of camping supplies
2/1/2026
"""


items: list[str] = [
    "tent",
    "sleeping bag",
    "air matress",
    "backpack",
    "food",
    "water",
    "extra clothes",
    "lighter",
    "flashlight",
    "first aid kit"
]


if __name__ == "__main__":
    print(f"Total number of items: {len(items)}")
    print(f"Items in alphabetical order: {sorted(items)}")