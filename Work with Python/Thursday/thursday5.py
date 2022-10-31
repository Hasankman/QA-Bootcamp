sauron = {"name" : "Sauron", "no_rings" : 1, "ring_missing" : True, "address" : "Mordor", "popularity" : -1.025}

print(type(sauron))
print(sauron)

gandalf = {"name" : "Gandalf", "ring_missing" : False}
print(gandalf)

gandalf["address"] = "none"
gandalf["no_rings"] = 1
gandalf["popularity"] = 98.27

print(gandalf)


if "address" in sauron:
    print(sauron["address"])
else:
    print("sauron does not have a address")


print("iterating through all the keys: ")

for key in gandalf.keys():
    value = gandalf[key]
    print(key, "=", value)
