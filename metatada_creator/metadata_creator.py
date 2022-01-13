import json
import os
import os.path

files = glob.glob(r"D:\GitHub\projectspython\Pythonprojects\metatada_creator\pics**")
for file in files:
    # Get the name of the file less any suffixes
    name = os.path.basename(file).split('.')[0]
    
    # Serializing json 
    json_object = json.dumps(dictionary, indent = 4)
  
    # Writing to sample.json
    with open(name, "w") as outfile:
    outfile.write(json_object)
    # Use `name` from above to name your text file         
    with open("D:\GitHub\projectspython\Pythonprojects\metatada_creator\pics**" + name + ".txt", 'w') as f:
        f.write(str(extracted_texts))


generate_unique_images(11, {
    
    "baseURI": ".",
    "name": "Faces #",
    "description": "Random faces made by me.",
    "file": "",
    
}