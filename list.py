#  list
food = list(("githeri", "shawarma", "kebab", "apple", "cherry"))
print(food)
print(list[1:2])
food[1:3] = ["tai", "watermelon"]
print(food)
food.insert(3,"passion")
print(food)

#  dictionary
emotions = {"name": "happiness",
            "cause": "satisfaction",
            "date": "67/75/2099"
            }
print(emotions)
print(emotions.keys())
print(emotions.values())
print(emotions.items())
if "name" in emotions:
    print("yes... name exists")
for x in emotions:
    print(emotions[x])
