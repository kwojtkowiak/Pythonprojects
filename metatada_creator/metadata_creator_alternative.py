import json
import os
import os.path

#don't even know what that piece of code does lol
os.system('cls' if os.name=='nt' else 'clear')

#input directory and creaty empty list for iterating through all files in the folder and filtering .png files (easily adjustable to other types)
dir_with_files = "./metatada_creator/pics"
picfiles=[f for f in sorted(os.listdir(dir_with_files)) if (str(f))[-3:] == "png"]
picfiles_with_path=[dir_with_files+'/'+str(f) for f in picfiles]  

number_of_pics = len(picfiles)
print("Number of detected files: {}".format(number_of_pics))

#Main meat - function to generate metadata file for every single picture in dir based on information provided in config object
def generate_unique_metadata(number_of_pics, config):
    print("Generating {} unique metadata files".format(number_of_pics))
    pad_amount = len(str(number_of_pics));
#stworzyc druga liste i tuple z linkami do .png
    for i, pic in enumerate(picfiles,1):
        outfile_name = pic[:-4] 
        token_metadata = {
            "name":  config["name"] + str(i).zfill(pad_amount),
            "description": config["description"],
            "file": config["file"],
            "attributes": [{"type":"name","value":outfile_name}]
        }
        with open ("./metatada_creator/pics/" + outfile_name + ".json", 'w+') as outfile:
            json.dump(token_metadata, outfile)
            

generate_unique_metadata(131, {
    "name": "PTH #",
    "description": "The collection of PictoHeads, courtesy to Epiq NFT",
    "file": "/ipfs/QmSkMeKsFrQ6K7p8W43FcMHa4ji4sEpmcpbF3qqoSuSwZU",
})

print("Operation succesful")