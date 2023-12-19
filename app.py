from web3 import Web3

# Connect to Ethereum - replace with your Ethereum node
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

# Replace with your contract address and ABI
contract_address = '0xYourContractAddress'
contract_abi = 'YourContractABI'

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def create_role(role_name):
    tx_hash = contract.functions.createRole(web3.toBytes(text=role_name)).transact()
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def assign_user_to_role(role_name, user_address):
    tx_hash = contract.functions.assignUserToRole(web3.toBytes(text=role_name), user_address).transact()
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def grant_permission_to_role(role_name, permission):
    tx_hash = contract.functions.grantPermissionToRole(web3.toBytes(text=role_name), web3.toBytes(text=permission)).transact()
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def check_user_permission(user_address, permission):
    return contract.functions.hasPermission(user_address, web3.toBytes(text=permission)).call()

# Example usage
create_role('Administrator')
assign_user_to_role('Administrator', '0xUserAddress')
grant_permission_to_role('Administrator', 'view_dashboard')
print(check_user_permission('0xUserAddress', 'view_dashboard'))
