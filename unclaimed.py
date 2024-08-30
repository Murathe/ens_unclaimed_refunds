import logging
from web3 import Web3

#Configure logging
logging.basicConfig(level=logging.INFO)

# connect to infura since i don't have a node
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# ENS Auction contrcat address and abi
ens_auction_contract_address = 'ensContrcatADDRESS'
ens_auction_abi = [
    #abi goes here
]

# initialize the contract
contract = web3.eth.contract(address=ens_auction_contract_address, abi=ens_auction_abi)


def get_unclaimed_refunds():
    try:
        events = contract.events.BidRevealed.createFilter(fromBlock=0, toBlock='latest').get_all_entries()

        for event in events:
            bidder_address =event['args']['bidder']
            refund = contract.functions.refunds(bidder_address).call()

            if web3.fromWei(refund, 'ether') > 0:
                logging.info(f"cunlaimed refund for {bidder_address}: {web3.fromWei(refund, 'ether')} ETH")
    except Exception as e:
        logging.error(f"kuna makosa imefanyika")