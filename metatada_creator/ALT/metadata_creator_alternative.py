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

#Main meat - function to generate metadata file for every single picture in dir based on information provided in config object
def generate_unique_metadata(number_of_pics, config):
    print("Generating {} unique metadata files".format(number_of_pics))
    pad_amount = len(str(number_of_pics));
    #counting pictures
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
            "image": config["file"] + "/images/" + str(token["tokenId"]) + '.png',
            "tokenId": token["tokenId"],
            "name":  config["name"] + str(token["tokenId"]).zfill(pad_amount),
            "description": config["description"],
            "attributes": attributes
        }
        with open('./metadata/' + str(token["tokenId"]) + '.json', 'w') as outfile:
            json.dump(token_metadata, outfile, indent=4)
    
    with open('./metadata/all-objects.json', 'w') as outfile:
        json.dump(picfiles, outfile, indent=4)
    
    # CID generator
    print("\n Metadata files created. After uploading images to IPFS, please paste the CID below.\nYou may hit ENTER or CTRL+C to quit.")
    cid = input("IPFS Image CID (): ")
    if len(cid) > 0:
      if not cid.startswith("ipfs://"):
        cid = "ipfs://{}".format(cid)
    if cid.endswith("/"):
        cid = cid[:-1]
    for i, token in enumerate(picfiles):
      with open('./metadata/' + str(item["tokenId"]) + '.json', 'r') as infile:
        original_json = json.loads(infile.read())
        original_json["image"] = original_json["image"].replace(config["baseURI"]+"/", cid+"/")
        with open('./metadata/' + str(item["tokenId"]) + '.json', 'w') as outfile:
          json.dump(original_json, outfile, indent=4)

generate_unique_metadata(15, {
    "name": "TST #",
    "description": "Test test ",
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
})