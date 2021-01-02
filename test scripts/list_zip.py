#list zip test
#from itertools import *

receiver = "stoo,fish,plee,timp"
percents = "20,10,15,15" # find a way to auto add 0, since itertools doesn't import

rl = receiver.split(',')
pl = percents.split(',')

amount = 500
sender = 0
newamount = 0
val = 0
total = 0
for n in pl:
    val += int(n)

rem = 100 % val
    # somehow limit and bring the last amount to no more than 100%

if rem == 100:
    print('quantity too high') #and pass / retry / reject
else:

    result = list(zip(rl, pl))
    print('original amount', amount)
    print('value', val)
    print('remainder', rem)
    sender -= (val/100) * amount
    print('Sender amount', sender)
    for i in result:
        print('percentage', i[1])
        newamount = round(amount * (int(i[1]) / 100)) #might need to round it
        total += newamount
        print('new amount', newamount)

    print('final amount', amount)
    print('final total', total)
