import random
"┌─────────┐"
"│         │"
"│    ●    │"
"│         │"
"└─────────┘"


dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●  ●  ● │",
        "│         │",
        "│ ●  ●  ● │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for pie in range(num_of_dice):
    dice.append(random.randint(1, 6))

''' for pie in range(num_of_dice):
    for line in dice_art.get(dice[pie]):
        print(line)
'''

for line in range(5):
    for pie in dice:
        print(dice_art.get(pie)[line], end="")
    print()

for pie in dice:
    total += pie
print(f"total: {total}")