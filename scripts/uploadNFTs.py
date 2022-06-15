
import os
import json
import requests
from os import listdir
from pathlib import Path
from urllib import response
from NFTs.JSON_Template import JSON_template

#Global Variables
General_Description = "Thank you for your kind gesture"
NFTLocation = "./NFTs/"

def main():


    print("Creating JSON files and uploading")
    

    # get the path/directory
    folder_dir = NFTLocation
    NFT_List = []
    for images in os.listdir(folder_dir):
    # check if the image ends with png
        if (images.endswith(".jpg")):
            image = os.path.splitext(images)[0]
            print(f"Processing {image}")
            ## JSON_template_FIle
            JSON_template_file = f"{folder_dir}{image}.json"
            MetaData = JSON_template
  
            MetaData["name"] = image
            MetaData["description"] = General_Description
            MetaData["image"] = uploadToIPFS(f"{folder_dir}{images}")
            uploadToPinata(f"{folder_dir}{images}")
            
            with open(JSON_template_file, 'w') as f:
                    json.dump(MetaData, f, indent=2)
                    f.close()
            NFT_List.append(uploadToIPFS(JSON_template_file))
            uploadToPinata(JSON_template_file)
    #SaveGlobalList
    print(NFT_List)
    with open(f"{folder_dir}NFT_List.json", 'w') as f:
                                json.dump(NFT_List, f, indent=2)
                                f.close()
            

def uploadToPinata(filename):
    PINATA_BASE_URL = "https://api.pinata.cloud/"
    endpint = "pinning/pinFileToIPFS"
    file = filename.split("/")[-1:][0]
    header = {"pinata_api_key": os.getenv("PINATA_API_KEY"),"pinata_secret_api_key": os.getenv("PINATA_Secret_API_KEY")}
    with Path(filename).open("rb") as fp:
        image_binary = fp.read()
        requests.post(PINATA_BASE_URL + endpint,files={"file": (file,image_binary)},headers=header)


def uploadToIPFS(filename):
    with Path(filename).open("rb") as fb:
        image_binary = fb.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        responce = requests.post(ipfs_url + endpoint, files={"file": image_binary})
    
        ipfs_hash = responce.json()["Hash"]
        filename = filename.split("/")[-1:][0]
        image_uri= f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        return image_uri