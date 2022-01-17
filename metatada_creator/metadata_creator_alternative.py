import json
import os
import os.path

#don't even know what that piece of code does lol
os.system('cls' if os.name=='nt' else 'clear')

#input directory and creaty empty list for iterating through all files in the folder
path = "D:\GitHub\projectspython\Pythonprojects\metatada_creator\pics"
files = os.listdir(path)
picfiles = []
number_of_pics = len(picfiles)

#Creating empty list of files for future use
for file in files:
    picfiles.append(file)

#Main meat - function to generate metadata file for every single picture in dir based on information provided in config file
def generate_unique_metadata(number_of_pics, config):
    print("Generating {} unique metadata files".format(number_of_pics))
    pad_amount = len(str(number_of_pics));

    i = 1
    for item in picfiles:
        item["tokenId"] = i
        i += 1

    for i, token in enumerate(picfiles):
        attributes = []
        for key in token:
            if key != "tokenId":
                attributes.append({"trait_type": key, "value": token[key]})
        token_metadata = {
            "image": config["baseURI"] + "/images/" + str(token["tokenId"]) + '.png',
            "tokenId": token["tokenId"],
            "name":  config["name"] + str(token["tokenId"]).zfill(pad_amount),
            "description": config["description"],
            "attributes": attributes
        }

#Example metadata requirements
{
    "name": "FAC #",
    "description": "Collection of PictoHeads I've made.",
    "file": "<tu bedzie link>",
    "attributes": [
        {
            "type": "rarity",
            "value": "super rare"
        },
        {
            "type": "title",
            "value": "CEO"
        }
    ]
}