import json


# Users will need to install web3 and eth_account
# `pip install web3`
from web3 import Web3


# Users will need to create a free account at Infura (https://infura.io/) 
#  to be able to access an ethereum endpoint. 
PROVIDER_ENDPOINT = "https://mainnet.infura.io/v3/<INFURA_KEY_HERE>"


# Instantiate the Web3 class using the custom endpoint
web3 = Web3(Web3.HTTPProvider(PROVIDER_ENDPOINT))


# Users will also need to provide their private key (provided at event) with 
#  enough ether to make a request from the contract.
PRIVATE_KEY = "<PRIVATE_KEY_HERE>"


# Use web3.eth.account library to derive the public address from the key.
# 
# https://web3py.readthedocs.io/en/stable/web3.eth.account.html
ACCOUNT = web3.eth.account.privateKeyToAccount(PRIVATE_KEY)
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

###############################################################################
print("Building a Raw Transaction")

# Functions that only read data from the blockchain can be invoked with the .call() function.
# Functions that will modify the blockchain state will need to be prepared as transactions.

# Now we're going to make our first transaction. This will prepare a raw transaction that requests
#  one ColumbusToken from the contract!

# First we will want to set some transaction variables.

# We'll use this variable to set the maximum amount of gas to be used in the transaction. This
#  generally prevents your costs from unexpectedly getting out of control by killing the transaction
#  when the gas limit is exceeded.
# For the ColumbusToken, invoking the getToken() method should cost around 69476 gas, so we'll estimate
#  just a little more than that.
maximum_gas = 100000

# A nonce value is required for each transaction. It prevents duplicate transactions from being processed
#  by the network and ensures that transactions are processed in the intended order. The nonce has a
#  0-index and should be equal to the number of transactions sent by the account.
# We can use web3's getTransactionCount(address) function to get the nonce value for a transaction.
nonce = web3.eth.getTransactionCount(ACCOUNT.address)
print(f"nonce: {nonce}")

# The chainId is the id of the network we are deploying to, examples:
#   1 : Ethereum Mainnet
#   3 : Ropsten Testnet
#   4 : Rinkeby Testnet
# The web3 call returns the value as a string, but we will need an integer to create a transaction.
chain_id = int(web3.version.network)
print(f"Chain ID: {chain_id}")


# Gas price is defined programatically in wei, but it's typically discussed in GWEI.
#  Luckily, web3 provides us a method to quickly convert gwei to wei.
#  Users may want to check https://ethgasstation.info/ prior to sending a transaction
#  to ensure that they don't set too high or low a price.
#  A gas price that's too high can incur needless expense.
#  A price that's too low will mean that your transaction takes longer to process, and
#  if it's very low it may never get processed at all.
gas_price = web3.toWei('10', 'gwei')
print(f"Gas Price: {gas_price} wei")


# We're now going to build the transaction to request a ColumbusToken.
# We will first build a raw transaction containing the data to be transmitted, and then
#  we will cryptographically sign the transaction with our private key.
#  
#  https://web3py.readthedocs.io/en/stable/contracts.html#web3.contract.ContractFunction.buildTransaction
#
# The ColumbusToken contract contains a unique (and nonstandard) feature that allows
#  an account to claim one CBUS token once upon request. This can actually be abused pretty
#  easily so it's just a fun way to demonstrate interacting with a smart contract.
#
# See Line 57 of the code at:
# https://etherscan.io/address/0x07c344edd719a356775e1fbd852c63dc46167b76#code 
#
#      function getToken() public {
#        // Don't allow more tokens to be created than the maximum supply
#        require(_totalSupply < max_supply);
#        // Don't allow the requesting address to request more than one token.
#        require(_requested[msg.sender] == false);
#        
#        _requested[msg.sender] = true;
#        _balances[msg.sender] += _tokens(1);
#        _totalSupply += _tokens(1);
#        
#        emit GeneratedToken(msg.sender);
#      }
raw_transaction = columbusTokenContract.functions.getToken().buildTransaction({
    'chainId': chain_id,
    'gas': maximum_gas,
    'gasPrice': gas_price,
    'nonce': nonce
})
print(f"Raw Transaction: {raw_transaction}\n")
# Raw Transaction: {'value': 0, 'chainId': 1, 'gas': 100000, 'gasPrice': 10000000000, 
#  'nonce': 0, 'to': '0x07c344edD719A356775E1FBd852c63Dc46167B76', 'data': '0x21df0da7'}


# Sign the raw transaction using your private key using your web3 acount object
signed_transaction = ACCOUNT.signTransaction(raw_transaction)
print(f"Signed Transaction: {signed_transaction}\n")
# Signed Transaction: AttrDict({'rawTransaction': 
#  HexBytes('0xf86980850........76ae1525a0'), 
#  'hash': HexBytes('0xa1845a370.......0d6b93f7727035f883cfa'), 
#  'r': 93095648781695009.......6984224547883143517748, 
#  's': 4683787713977.....27619885118225990304441992291744,
#  'v': 38})


# Your signed transaction contains everything it needs to be processed by the network.
# To get your CBUS Token, uncomment the following line to submit the transaction.
#  (Ensure that there is some ether in your account!)
# Once the transaction has processed, go back and check your CBUS token balance.
#transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)
#print(f"Transaction Hash: {transaction_hash}\n")
