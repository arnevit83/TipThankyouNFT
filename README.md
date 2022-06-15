# Tip contract and get a random AI Generation NFT

Here is an example project of a etherium contract running on Brownie

Here is a working [example](https://duncanpeach.com/)

## Installation

Use the package manager [Brownie](https://eth-brownie.readthedocs.io/en/stable/) to install foobar.

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install eth-brownie

```

## Usage

```python
# Compiles contracts
brownie compile

# returns 'words'
brownie test

# Deploys to Rinkeby
brownie run scripts/deploy.py --networks rinkeby

# Deploys to Ganashe
brownie run scripts/deploy.py

# Loads All imaages to IPFS and Pinyata and creates NFT TokenURI files
# Requites IPFS diamon running
brownie run scripts/uploadNFTs.py

```

## More Info

Contract can be found [Here](https://etherscan.io/address/0x2ddD77B20F0ee65bb68dc5DdE863135350ea3e8B#code)

If you need any web3 work please get in touch [https://duncanpeach.com/](https://duncanpeach.com/)

## License

SPDX-License-Identifier: Apache License 2.0
