from scripts.generic import loadAccounts,local_BlockCahins,network,TipThankyouNFT
from web3 import Web3;

def test_sendTipForNFT():
    # Arrange
    CVContract= TipThankyouNFT()
    wallet = loadAccounts();
    #Act
    minimalTipPriceinEth = CVContract.getPrice()
    Ethprice_TX = CVContract.sendTipForNFT({"from": wallet, "value": minimalTipPriceinEth + 100000})
    Ethprice_TX.wait(1)
    #Assert
    assert CVContract.Tippers(0) == wallet

def test_getMinimalPrice():
    # Arrange
    CVContract= TipThankyouNFT()
    #Act
    minimalTipPriceinEth = CVContract.getPrice()
    #Assert
    assert minimalTipPriceinEth > Web3.toWei(0.02,"ether")
    assert minimalTipPriceinEth < Web3.toWei(0.03,"ether")
    
def test_NFTCreation():
    # Arrange
    if (network.show_active()) not in local_BlockCahins:
        pytest.skip()
    NFTContract = TipThankyouNFT()
    wallet = loadAccounts();
    #Act
    NFT = NFTContract.CreateThankyouNFT({"from": wallet})
    NFT.wait(1);
    #Assert
    assert NFTContract.ownerOf(0) == wallet