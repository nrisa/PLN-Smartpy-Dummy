from pytezos import pytezos

# Hubungkan ke node Tezos
pytezos = pytezos.using(shell='https://mainnet-tezos.giganode.io', key='your_private_key')

# Alamat kontrak yang di-deploy
contract_address = 'KT1VYamXFv7A9nEbPA3ZNpVYqsc5PS5BYNZJ'

def add_customer_to_contract(customer_data):
    contract = pytezos.contract(contract_address)
    operation = contract.add_customer(customer_data).send(min_confirmations=1)
    return operation

def get_customer_from_contract(customer_id):
    contract = pytezos.contract(contract_address)
    return contract.get_customer(customer_id).storage()
