import smartpy as sp

class DummyTokenContract(sp.Contract):
    def __init__(self):
        self.init(tokens = sp.big_map())

    @sp.entry_point
    def check_customer(self, params):
        sp.verify(params.customer_id.is_some())
        sp.verify(params.amount > 0)
        self.data.tokens[params.customer_id] = params.amount

@sp.add_test(name = "DummyTokenContract")
def test():
    scenario = sp.test_scenario()
    contract = DummyTokenContract()
    scenario += contract
    scenario += contract.check_customer(customer_id = "12345", amount = 100)
