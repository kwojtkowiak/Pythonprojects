import json
import os
import os.path

#don't even know what that piece of code does lol
os.system('cls' if os.name=='nt' else 'clear')

#input directory and creaty empty list for iterating through all files in the folder
path = "./metatada_creator/pics"
picfiles = os.listdir(path)
#stworzyc filtrowanie plikow graficznych

number_of_pics = len(picfiles)
print("Number of detected files: {}".format(number_of_pics))

#Main meat - function to generate metadata file for every single picture in dir based on information provided in config object
def generate_unique_metadata(number_of_pics, config):
    print("Generating {} unique metadata files".format(number_of_pics))
    pad_amount = len(str(number_of_pics));
#stworzyc druga liste i tuple z linkami do .png
    for i, pic in enumerate(picfiles,1): 
        token_metadata = {
            "name":  config["name"] + str(i).zfill(pad_amount),
            "description": config["description"],
            "file": config["file"]
        }
        outfile_name = pic[:-4] + ".json"
        with open ("./metatada_creator/ALT/pics/" + outfile_name, 'w+') as outfile:
            json.dump(token_metadata, outfile)
            

generate_unique_metadata(131, {
    "name": "PTH #",
    "description": "The collection of PictoHeads, courtesy to Epiq NFT",
    "file": "/ipfs/QmSkMeKsFrQ6K7p8W43FcMHa4ji4sEpmcpbF3qqoSuSwZU",
})

print("Operation succesful")