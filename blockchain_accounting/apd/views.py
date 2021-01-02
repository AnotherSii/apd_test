from django.shortcuts import render
#from apd.static.smartcontract import *
from django.views.generic import CreateView
import lampy
import lamdenpy
import contracting
# from lampy import *
# from lampy import Wallet
from lamdenpy.query import *
from lamdenpy.wallet import * #Wallet, Connection
from blockchain_accounting.settings import *

#time to svelte

# Create your views here.
ip_status = production_dictionary[production_status]['ip']
sk = production_dictionary[production_status]['sk'] #to be replaced by a model later

wallet = Wallet()

msg = 'goose'

vk = wallet.vk
sk = wallet.sk

client = Connection(ip=ip_status, wallet=wallet)

class APD_Test(CreateView):
    template_name = 'apd/test.html'
    
    def get(self, request):
        contracts = client.get_contracts()
        testDict = { 'contracts': contracts, 'vk': vk, 'sk': sk, }
        return render(request, 'apd/test.html', testDict) #e template might not work
    
    def post(self, request):

        # are these necessary?
        #wallet.vk.encode()
        #wallet.pk.encode()
        

        #client_2 = Connection(ip=ip_status)

        #client_1.get_latest_block_hash() == client_2.get_latest_block_hash()
        
        
        
        testDict = {'contracts': '' }
        return render(request, 'apd/test.html', testDict)
    
    
class BillPay():
    template = 'apd/bills.html'
    
    def get(self, request):
        # maybe automate the smart contract process, allow people to pay two whomever (in exact payments, not percentages
        
        return(render, 'apd/bills.html')
    
    def post(self, request):
        return(render, 'apd/bills.html')