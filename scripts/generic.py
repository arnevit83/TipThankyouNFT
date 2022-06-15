
from brownie import accounts,config,network,network,MockV3Aggregator,TipThankyouNFT
import json
#Global Variables
local_BlockCahins = ["development","ganache-local-gui"]
NFTLocation = "./NFTs/"

def loadAccounts():
    wallet = None;
    if network.show_active() in local_BlockCahins:
        wallet = accounts[0]
    else:
        wallet = accounts.add(config["accounts"]["Metamask_dev"])
    print(f"Account Selected: { wallet }")
    return wallet;

def DeployTipThankyouNFT():  
    ThankyouNFT = None;
    wallet = loadAccounts();
    print(f"Using network: { network.show_active() }") 
    with open(NFTLocation +  "NFT_list.json", 'r') as f:
            data = json.load(f)
            f.close()
    if network.show_active() not in local_BlockCahins:
        print("Deploying: TipThankyouNFT")         
        ThankyouNFT = TipThankyouNFT.deploy(data,config["networks"][network.show_active()]["USDETHFeed"],{"from": wallet},publish_source=config["networks"][network.show_active()]["verify"])      
    else:
        if len(MockV3Aggregator) <= 0:
            print("Deploying: MockV3Aggregator") 
            MockV3Aggregator.deploy(18,2000000000000000000000,{"from": wallet})
        print("Deploying: TipThankyouNFT")         
        ThankyouNFT= TipThankyouNFT.deploy(data,MockV3Aggregator[-1].address,{"from": wallet},publish_source=config["networks"][network.show_active()]["verify"])
    return ThankyouNFT 
