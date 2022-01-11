import json
import os
import os.path

def generate_metadata(amount, config):
    print("Generating {} .json files".format(amount))

generate_unique_images(11, {

    "name": "obiyankenobi",
    "description": "Cool art for @obiyankenobi, courtesy of @PixtarsHathor",
    "file": "ipfs://ipfs/QmYKrVVCdmf1tkThbmny1M8JHVGrLdWNnXhCnrUUrvzsZa",
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