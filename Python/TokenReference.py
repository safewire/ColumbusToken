import json


# Users will need to install web3 and eth_account
# `pip install web3`
# `pip install eth_account`
from web3 import Web3
from eth_account import Account


# Users will need to create a free account at Infura (https://infura.io/) 
#  to be able to access an ethereum endpoint. 
PROVIDER_ENDPOINT = "https://mainnet.infura.io/v3/<INFURA_KEY_HERE>"


# Instantiate the Web3 class using the custom endpoint
web3 = Web3(Web3.HTTPProvider(PROVIDER_ENDPOINT))


# Users will also need to provide their private key (provided at event) with 
#  enough ether to make a request from the contract.
PRIVATE_KEY = "<PRIVATE_KEY_HERE>"

# Use the eth_account library to derive the public address from the key
# Web3.py doesn't include an option to convert a private key to a wallet address
#  in memory, so we're relying on the Account object from the eth_account library
ACCOUNT = Account.privateKeyToAccount(PRIVATE_KEY)
print(f"Wallet address: {ACCOUNT.address}")


# Now that we have an account, let's use Web3.py to check the balance.
wei_balance = web3.eth.getBalance(ACCOUNT.address)
# Ethereum measures eth in wei, which is the smallest unit that it's divisible by.
# 1 Ether = 1000000000000000000 Wei
# Similarly, when working with the ColumbusToken you'll find that it's also divisible
#  by 18 places. Web3.py provides a helper for converting this to a balance denominated in ether.
eth_balance = web3.fromWei(wei_balance, "ether")
print(f"ETH balance: {eth_balance}")


# This is the address of the deployed ERC-20 contract. This should not be changed.
# The new version of Web3 requires that we parse the address to a checksum address.
CONTRACT_ADDRESS = Web3.toChecksumAddress('0x07c344edd719a356775e1fbd852c63dc46167b76')


# Users load the ABI content from a provided file:
import os
CONTRACT_ABI = ""
with open(os.path.join(os.path.dirname(__file__), 'ColumbusTokenAbi.json')) as json_data:
    abi_json = json.load(json_data)
    # The provided abi was taken from etherscan, which has some extra stuff in it.
    # We just want the 'result' for creating a contract object.
    CONTRACT_ABI = abi_json['result']
#print(CONTRACT_ABI)


# Alternatively, you could have them go to etherscan and "Export ABI" into "JSON Format"
# https://etherscan.io/address/0x07c344edd719a356775e1fbd852c63dc46167b76#code
# Then paste it in here:
abi_json = {"status":"1","message":"OK","result":"[{\"constant\":true,\"inputs\":[],\"name\":\"name\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"spender\",\"type\":\"address\"},{\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"approve\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"getBalance\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"totalSupply\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[],\"name\":\"getToken\",\"outputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"from\",\"type\":\"address\"},{\"name\":\"to\",\"type\":\"address\"},{\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"transferFrom\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"decimals\",\"outputs\":[{\"name\":\"\",\"type\":\"uint8\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"spender\",\"type\":\"address\"},{\"name\":\"addedValue\",\"type\":\"uint256\"}],\"name\":\"increaseAllowance\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"owner\",\"type\":\"address\"}],\"name\":\"balanceOf\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"max_supply\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[],\"name\":\"symbol\",\"outputs\":[{\"name\":\"\",\"type\":\"string\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"spender\",\"type\":\"address\"},{\"name\":\"subtractedValue\",\"type\":\"uint256\"}],\"name\":\"decreaseAllowance\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":false,\"inputs\":[{\"name\":\"to\",\"type\":\"address\"},{\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"transfer\",\"outputs\":[{\"name\":\"\",\"type\":\"bool\"}],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"constant\":true,\"inputs\":[{\"name\":\"owner\",\"type\":\"address\"},{\"name\":\"spender\",\"type\":\"address\"}],\"name\":\"allowance\",\"outputs\":[{\"name\":\"\",\"type\":\"uint256\"}],\"payable\":false,\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[],\"payable\":false,\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"name\":\"from\",\"type\":\"address\"},{\"indexed\":true,\"name\":\"to\",\"type\":\"address\"},{\"indexed\":false,\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Transfer\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"name\":\"owner\",\"type\":\"address\"},{\"indexed\":true,\"name\":\"spender\",\"type\":\"address\"},{\"indexed\":false,\"name\":\"value\",\"type\":\"uint256\"}],\"name\":\"Approval\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"name\":\"requester\",\"type\":\"address\"}],\"name\":\"GeneratedToken\",\"type\":\"event\"}]"}
# We'll need to extract out the 'result' field, as above.
CONTRACT_ABI = abi_json['result']
#print(CONTRACT_ABI)


# Instantiate a web3 Contract object for working with the contract.
# address is the address where the contract is deployed on the network
# abi is the application binary interface for the contract.
columbusTokenContract = web3.eth.contract(
    address=CONTRACT_ADDRESS, 
    abi=CONTRACT_ABI
    )


# Great! We have a contract object that we can work with. Let's get some
# data from the blockchain! 

# Let's make sure we're working with the ColumbusToken by making some calls
#  to the contract. These are "view" functions and can be called for free.
# All of the readable functions on this contract can be found at:
#  https://etherscan.io/address/0x07c344edd719a356775e1fbd852c63dc46167b76#readContract
contract_name = columbusTokenContract.functions.name().call()
print(f"Contract Name: {contract_name}")

contract_symbol = columbusTokenContract.functions.symbol().call()
print(f"Contract Symbol: {contract_symbol}")

contract_totalSupply = columbusTokenContract.functions.totalSupply().call()
print(f"Contract totalSupply: {contract_totalSupply}")

# We may also want to pass a parameter to a view function.
# Let's check our CBUS token balance
token_balance = columbusTokenContract.functions.balanceOf(ACCOUNT.address).call()
print(f"My CBUS balance: {token_balance}")
