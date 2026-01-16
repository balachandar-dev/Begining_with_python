# List
age = 25
has_licence = True
my_list = ["Alice", 25, age, has_licence]

name = my_list[0]
age = my_list[1]

has_licence = my_list[-1]

colors = ["red", "blue", "cyan", "teal"]

primary_colors = colors[0:2]

colors.append("green")

colors.remove("green")

colors.insert(2, "green")

colors.sort()

#Dictionary key-value

person = {
    "name": "Alice",
    "age": 25,
    "city": "Chennai"
}

person["name"]

person["name"] = "Dave"

del person["name"]

#tuples - immutable list

red_color = (255, 0, 0)
black_color = (0, 0, 0)
pi_value = 3.14

red_color[0]

# Sets - probably array
# no duplicates

numbers = {0, 1, 2, 3}
fruits = set(["apple", "banana"])

scores = [85, 90, 95, 85]
unique_sets = set(scores)

unique_sets.discard(85) # doesnt care 
unique_sets.remove(85) # error if it doesnt works 