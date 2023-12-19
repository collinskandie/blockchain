import web3

class AdminController:
    def __init__(self, blockchain_url):
        # Initialize a connection to the Ethereum blockchain
        self.w3 = web3.Web3(web3.HTTPProvider(blockchain_url))
        self.contract = None  # Reference to the smart contract

    def connect_to_contract(self, contract_address, contract_abi):
        # Connect to the smart contract on the blockchain
        self.contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

    def assign_role_on_blockchain(self, user_id, role_name):
        # Check if the admin is authorized to perform this action
        # (you can implement authorization logic)

        # Prepare the transaction to assign a role to a user
        transaction = self.contract.functions.assignRole(user_id, role_name).buildTransaction({
            'chainId': 1,  # Ethereum mainnet
            'gas': 2000000,  # Adjust gas limit as needed
            'gasPrice': self.w3.toWei('20', 'gwei'),
            'nonce': self.w3.eth.getTransactionCount(self.w3.eth.accounts[0]),  # Use admin's account
        })

        # Sign and send the transaction
        signed_transaction = self.w3.eth.account.signTransaction(transaction, private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        # Wait for the transaction to be mined and confirmed
        self.w3.eth.waitForTransactionReceipt(tx_hash)
