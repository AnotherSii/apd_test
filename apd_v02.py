# Smart Contract State
State = Hash(default_value=0)

@construct
def seed(vk: str, amount: int): #it's almost like the seed needs to have the receiver wallets added....
    # initial token release
    State[vk] = amount
    # probably grab the balance from VK, instead of giving it tokens
    
# Extract method users can call
@export
def percent_transfer(amount: int, receivers: str, percentages: str): # find a better way to input the data
    sender = ctx.caller # ctx.caller is the verified person who signed the transaction
    balance = State[sender]
    assert balance >= int(amount), "Transfer amount exceeds available token balance"

    receiverlist = receivers.split(',')
    percentlist = percentages.split(',')
    users = list(zip(receiverlist, percentlist))

    # check remainder first, before it goes through
    val = 0
    for n in percentlist:
        val += int(n)

    rem = 100 % val

    assert rem != 100, "Percentages add up to greater than 100%" 

    # prevent sender tokens being sent into the aether
    State[sender] -= round(amount * (val/100))
    for i in users:
        State[i[0]] += round(amount * (int(i[1]) / 100))

@export
def amount_transfer(initial_amount: int, receivers: str, amounts: str):
    sender = ctx.caller # ctx.caller is the verified person who signed the transaction
    balance = State[sender]
    assert balance >= initial_amount, "Transfer amount exceeds available token balance"

    receiverlist = receivers.split(',')
    amountlist = amounts.split(',')
    users = list(zip(receiverlist, amountlist))

    val = 0
    for a in amountlist:
        val += int(a)

    assert balance >= val, "Not enough balance"

    State[sender] -= val
    for u in users:
        State[u[0]] += int(u[1])
