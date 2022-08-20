dictionary = {}
with open("C:/Users/Shaukat Issah/Desktop/words.txt") as file:
    lines = file.readlines()
    print(lines)
    del lines[0]
    print(lines)
    for line in lines:
        splits = line.strip("\n").split(",")
        print(splits)
        dictionary[splits[0]] = {
            "meaning": splits[1],
            "sy": splits[2],
            "anto": splits[3],
            "translation": {
                "french": splits[4],
                "twi": splits[5],
            }

        }

for key, value in dictionary.items():
    print(key, value)

# gui