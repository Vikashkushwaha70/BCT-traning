dic1 = {
    "name": "Vikash",
    "Add": "BR-29",
    "Mobile": 1234567890,
    "marks": [12, 13, 14, 15, 16]
}

# Printing the dictionary
print(dic1)

# Printing keys
print(dic1.keys())

# Printing values
print(dic1.values())

# Printing key-value pairs
print(dic1.items())

# Getting the value of the key "name"
print(dic1.get("name"))

# Updating the value of the key "Mobile"
dic1.update({"Mobile": 9931994688})

# Adding a new key-value pair "Gender" : "M"
dic1.update({"Gender": "M"})

# Printing the updated dictionary
print(dic1)
