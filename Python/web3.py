from web3 import Web3

url = "https://mainnet.infura.io/v3/c5aabd2edf83491dba28b57a13be8063"
web3 = Web3(Web3.HTTPProvider(url))

web3.isConnected()