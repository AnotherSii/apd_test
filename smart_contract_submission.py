"""
Contract Submission form

Can probably call this after someone enters and verifies addresses and amounts

@__export('submission')
def submit_contract(name: str, code: str, owner: Any=None, constructor_args: dict={}):
    assert not name.isdigit() and all(c.isalnum() or c == '_' for c in name), 'Invalid contract name!'
    __Contract().submit(name=name, code=code, owner=owner, constructor_args=constructor_args)


contractName: 'submission',
methodName: 'submit_contract',
kwargs: {
    name: "con_my_token",
    code: "contact code here",
    constructor_args: {
        "vk": "our public key",
        "amount": 1000000
    }
}

"""
