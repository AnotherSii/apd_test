import unittest
from contracting.client import ContractingClient

# make sure mongoDB is running with: sudo systemctl start mongod
client = ContractingClient()

filelocation = '/home/covenant/Documents/Lamden/Automated Pay Distribution/apd_v01.py' #main_file.py'
filename = 'apd' #'main_file' 

with open(filelocation) as f:
    code = f.read()
    client.submit(code, name=filename, constructor_args={'vk': 'me', 'amount': 50})

class MyTestCase(unittest.TestCase):

    def test_supply(self):
        contract = client.get_contract(filename)
        supply = 50
        #print(contract.quick_read('State', 'me'), supply)

        self.assertEqual(contract.quick_read('State', 'me'), supply)

    def test_transfer(self):
        client.signer = 'me'
        contract = client.get_contract(filename)
        supply = 50 
        
        send_amount = 10
        sender_amount = supply - send_amount
        receiver_amount = 0 + send_amount

        contract.transfer(
            amount=10,
            receiver='you'
            )
        self.assertEqual(contract.quick_read('State', 'me'), sender_amount)
        self.assertEqual(contract.quick_read('State', 'you'), receiver_amount)

    def test_transfer_neg_insufficient_funds(self):
        client.signer = 'you'
        contract = client.get_contract(filename)
        
        me_balance_before = contract.quick_read('State', 'me')
        you_balance_before = contract.quick_read('State', 'you')

        transfer_amount = you_balance_before + 1

        self.assertRaises( AssertionError, lambda: contract.transfer(amount = transfer_amount, receiver = 'me') )
        self.assertEqual(contract.quick_read('State', 'me'), me_balance_before)
        self.assertEqual(contract.quick_read('State', 'you'), you_balance_before)

if __name__ == '__main__':
    unittest.main()
