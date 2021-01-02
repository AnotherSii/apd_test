# have main wallet/hash/address with certain oins

# have list of deposit addresses/hashes, and a quantity based value alteration, with pointing out a remiander of funds

# Smart Contract State
State = Hash(default_value=0)


def createList:
    user = Variable()
    owner.set('a certain amount of input')

@construct
def seed(vk: str, amount: int):
    # initial token release
    State[vk] = amount
    

# Extract method users can call
@export
def transfer(amount: int, receiver: str, percents: str): # find a better way to input the data
    sender = ctx.caller # ctx.caller is the verified person who signed the transaction
    balance = State[sender]
    string = "Transfer amount exceeds available token balance"
    assert balance >= int(amount), string # check out this assert function

    userinfo = []
    receiverlist = receiver.split(',')
    percentlist = percents.split(',')

    for r, p in zip(receiverlist, percentlist)
        userinfo.append((r, p))

    State[sender] -= amount

    for i in userinfo:
        State[i[0]] += amount * (i[1] / 100)

"""
# probably need this
@export
def balance_of(wallet_id: str):
    return balances[wallet_id]
"""

# what about "input"?

# ===== Distribution System ======

def receiver_list():
    counter = 0
    max_percent = 100
    NoneList = ['None', 'none', 'n', 'N']
    userList = []
    userAmountsList = []

    while counter < 1:
        newUser = input("""Enter New User (or None when finished):""") #this doesn't work on blockchain
        if newUser in NoneList:
            counter = 1
        else:
            userList.append(newUser)
            counter = 0
    #print(userList)

    for i in userList:
        # Will need to add percentage sliders and such
        remaining_percent = max_percent
        while max_percent > 0:
            user_percentage = input("""What percent for %s? %s remaining. """ % (i, str(max_percent)) )
            max_percent -= int(user_percentage)
        
            if (max_percent < 0):
                userAmountsList.append((i, remaining_percent)) 
            else:
                userAmountsList.append((i, user_percentage))
            break;

            #print('Current Values: ', userAmountsList)
        else:
            userAmountsList.append((i, 0))

    for p in userAmountsList
        seed(p[0], p[1])

"""
def storage():
    user = Hash()

    @construct
    def seed():
        user[vk]['address'] = vk
        user[vk]['percent'] = 25

    #print(userAmountsList)

    receiver_list()

def token():
    balances = Hash()

    @construct
    def mint():
        balances[ctx.caller] = 100

c = ContractingClient(signer='stu')
c.submit(token) # constructor_args={'owner': 'stu'}

t = c.get_contract('token')
t.balances['stu']
"""

