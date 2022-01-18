import json
import os
import os.path

#don't even know what that piece of code does lol
os.system('cls' if os.name=='nt' else 'clear')

#input directory and creaty empty list for iterating through all files in the folder
path = "D:\GitHub\projectspython\Pythonprojects\metatada_creator\ALT\pics"
files = os.listdir(path)
picfiles = []

#Creating empty list of files for future use
for file in files:
    picfiles.append(file)

number_of_pics = len(picfiles)
print("Number of detected files: {}".format(number_of_pics))

#Main meat - function to generate metadata file for every single picture in dir based on information provided in config object
def generate_unique_metadata(number_of_pics, config):
    print("Generating {} unique metadata files".format(number_of_pics))
    pad_amount = len(str(number_of_pics));

    for i, pic in enumerate(picfiles,1): 
        token_metadata = {
            "name":  config["name"] + str(i).zfill(pad_amount),
            "description": config["description"],
            "file": config["file"]
        }

        outfile_name = str(i) + ".json"
        with open ("./pics/" + outfile_name, 'w+') as outfile:
            json.dump(token_metadata, outfile)
        

generate_unique_metadata(131, {
    "name": "PTH #",
    "description": "The collection of PictoHeads, courtesy to Epiq NFT",
    "file": "<link>",
})

print("Operation succesful")