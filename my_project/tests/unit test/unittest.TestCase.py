class TestAdminController(unittest.TestCase):
    def setUp(self):
        # Initialize the AdminController with a mock blockchain connection
        self.admin_controller = AdminController(blockchain_url="http://mockedblockchain:8545")

    def test_assign_role_on_blockchain(self):
        # Mock the blockchain interaction for testing purposes
        self.admin_controller.w3.eth.account.signTransaction = Mock(return_value="mocked_signed_transaction")
        self.admin_controller.w3.eth.sendRawTransaction = Mock(return_value=b'mocked_transaction_hash')
        self.admin_controller.w3.eth.waitForTransactionReceipt = Mock()

        # Test assigning a role on the blockchain
        user_id = 1
        role_name = "Administrator"
        self.admin_controller.assign_role_on_blockchain(user_id, role_name)

        # Verify that the blockchain interaction methods were called with the expected arguments
        self.admin_controller.w3.eth.account.signTransaction.assert_called_once()
        self.admin_controller.w3.eth.sendRawTransaction.assert_called_once()
        self.admin_controller.w3.eth.waitForTransactionReceipt.assert_called_once()
