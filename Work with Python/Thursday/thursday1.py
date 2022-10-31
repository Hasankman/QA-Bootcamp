
# lists can be made up of different data types

our_list = ["a", "b", "c", 1, 1.5]

our_list.append("d")

our_list.insert(0, "this is first")

print(our_list)

our_list.pop(5)

print(our_list)

del our_list[2]

print(our_list)

is_there = "c" in our_list

print(is_there)

cool_cows = ["Winnie the Moo", "Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

# print(cool_animals[-1]) - Kevs answer

# print(cool_animals[-1 [-1]]) Anne's answer

print(cool_animals[-1][-1]) # Wills answer

print(len(cool_animals))

cool_sheep.clear()

print(cool_sheep)
print(cool_animals)
