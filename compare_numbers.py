import json, re


txt = """

"""


with open('numbers.json', 'r') as file:
    data = json.load(file)

# Print all keys in a for loop
for key in data.keys():
    if key in txt:
        print(f"[{key}] Found")


if True:
    numbers = re.findall(r'\b\d{4,}\b', txt)

    # Build the dictionary
    output = {number: {"is_working": True, "last_checked": 0} for number in numbers}

    # Save to JSON
    with open("mozambique_numbers.json", "w") as f:
        json.dump(output, f, indent=4)

    print(f"Saved {len(output)} numbers to mozambique_numbers.json")