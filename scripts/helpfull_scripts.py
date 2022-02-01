from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 300000000000
LOCAL_BLOCKCHAIN_ENV = ["development", "test-ganache-local"]
FORKED_LOCAL_ENV = ["mainnet-fork"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        account = accounts[0]
        print(f"[+] Using account: {account}")
        return account
    else:
        account = accounts.add(config["wallets"]["from_key"])
        print(f"[+] Using account: {account}")
        return account


def deploy_mock():
    print(f"\n[.] Active network: {network.show_active()}")
    print("[+] Deploying Mocks ...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("[+] Mock Deployed\n")
