import smartpy as sp

class PLNToken(sp.Contract):
    def __init__(self, owner):
        self.init(
            owner = owner,
            customers = sp.big_map(tkey=sp.TString, tvalue=sp.TRecord(customer_name=sp.TString, customer_id=sp.TString, meter_serial=sp.TString, token=sp.TString, price=sp.TNat))
        )

    @sp.entry_point
    def add_customer(self, params):
        sp.verify(sp.sender == self.data.owner)
        self.data.customers[params.customer_id] = sp.record(
            customer_name = params.customer_name,
            customer_id = params.customer_id,
            meter_serial = params.meter_serial,
            token = params.token,
            price = params.price
        )

    @sp.entry_point
    def get_customer(self, params):
        sp.result(self.data.customers[params.customer_id])

@sp.add_test(name = "PLN Token Test")
def test():
    scenario = sp.test_scenario()
    owner = sp.test_account("Owner")
    contract = PLNToken(owner.address)
    scenario += contract

    customer_id = "1234567890"
    customer_data = sp.record(
        customer_name = "John Doe",
        customer_id = customer_id,
        meter_serial = "A123456",
        token = "1234567890123456",
        price = 200000
    )

    scenario += contract.add_customer(customer_data).run(sender=owner)

    scenario.verify(contract.data.customers[customer_id].customer_name == "John Doe")
