"""
    -> the enumerate function
    -> this is for iterating through lists
"""

locations = ["Indonesia", "Spain", "Thailand", "Mexico", "USA"]
for index, country in enumerate(locations, start = 1): #starting at 1 is a workaround for Python being zero-indexed
    #this uses tuple unpacking
    print(f"* {index}: {country}")