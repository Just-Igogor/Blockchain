import web3
import json

from auth_manager import AuthManager

class API_RentalPlatform():
    w3 = web3.Web3(web3.HTTPProvider("http://127.0.0.1:8545"))

    contract_address = web3.Web3.to_checksum_address("0xF1bFFEEA61383555E05a966c8A1E019101837163")
    with open("abi.txt", "r") as f:
        abi = json.load(f)
    contract = w3.eth.contract(address=contract_address, abi=abi)

    admin_address = contract.functions.admin().call()
    nextItemId = contract.functions.nextItemId().call()
    nextRentId = contract.functions.nextRentId().call()

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
    
    def account(self):
        return self.w3.eth.accounts

    def get_balance(self, address):
        address = web3.Web3.to_checksum_address(address)
        return self.contract.functions.balanceOf(address).call()

    def get_admin(self):
        return self.contract.functions.admin().call()

    def get_item(self, item_id):
        item = self.contract.functions.rentalItems(int(item_id)).call()
        return item

    def list_Item(self, name, description, pricePerDay, address_from):
        tx = self.contract.functions.listItem(name, description, pricePerDay).transact({"from" : address_from})
        self.w3.eth.wait_for_transaction_receipt(tx)
        return

    def rent_Item(self, item_id, durationDays, address_from):
        item = api.get_item(item_id)
        cost = durationDays * item[5]
        tx = self.contract.functions.rentItem(item_id, durationDays).transact({"from" : address_from, 'value' : cost})
        self.w3.eth.wait_for_transaction_receipt(tx)
        return

    def get_RentedFromUser(self, address):
        address = web3.Web3.to_checksum_address(address)
        return self.contract.functions.getRentedFromUser(address).call()

    def get_RentedForUser(self, address):
        address = web3.Web3.to_checksum_address(address)
        return self.contract.functions.getRentedForUser(address).call()

    def get_RentalRecord(self, num):
        return self.contract.functions.allRentalRecords(num).call()

    def give_TokensToUser(self, address_to, amount):
        address = web3.Web3.to_checksum_address(self.admin_address)
        tx = self.contract.functions.giveTokensToUser(address_to, amount).transact({"from" : address})
        self.w3.eth.wait_for_transaction_receipt(tx)
        return
    
    def unlock_account(self, address, password):
         self.w3.geth.personal.unlock_account(address, password, 0)


"""
    def get_token_balance(self, address):
        balance = self.get_balance(address)
        return balance

    def get_nickname(self, address):
        users = self.load_users()
        for user in users["users"]:
            if user["eth_address"] == address:
                return user["login"]
        

api = API_RentalPlatform()
user0 = api.account()[0]
api.unlock_account(user0, "1234")
print(user0)
balance = api.get_balance(user0)
print(balance)
print(api.get_admin())
api.list_Item("Biba", "gfchjkl", 1, api.account()[0])
print(api.get_item(1))

api = API_RentalPlatform()
user0 = api.account()[1]
api.unlock_account(user0, "1234")
print(user0)
balance = api.get_balance(user0)
print(balance)
print(api.get_admin())
api.give_TokensToUser("0xC450AA1ADe2C6F3B4423B64267648E9b64115BA3", 1000)
balance = api.get_balance(user0)
print(balance)

api = API_RentalPlatform()
print(api.contract.functions.allRentalRecords(0).call())

api = API_RentalPlatform()
auth_manager = AuthManager()
users = auth_manager.load_users()
print(users)
address = '0xC450AA1ADe2C6F3B4423B64267648E9b64115BA3'
print(api.get_token_balance(address))
print(api.get_nickname(address))
"""
