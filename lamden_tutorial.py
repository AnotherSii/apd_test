# Smart Contract State
State = Hash(default_value=0)

@construct
def seed(vk: str, amount: int):
    # initial token release
    State[vk] = amount
    

# Extract method users can call
@export
def transfer(amount: int, receiver: str): # apparently you assign data types this way.. nice
    sender = ctx.caller # ctx.caller is the verified person who signed the transaction
    balance = State[sender]
    string = "Transfer amount exceeds available token balance"
    assert balance >= int(amount), string # check out this assert function
    
    State[sender] -= amount
    State[receiver] += amount
