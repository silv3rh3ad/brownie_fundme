from distutils.command.config import config
from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpfull_scripts import deploy_mock, get_account, LOCAL_BLOCKCHAIN_ENV


def deploy_fundme():
    print("[.] Deploying FundMe Contract ... ")
    account = get_account()
    print("[+] Checking Active Network")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENV:
        print(
            f"\n[.] Active network: {network.show_active()} \n[+] No Mocking required"
        )
        price_feed_address = config["networks"][network.show_active()].get(
            "eth_usd_price_feed"
        )
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    fundme = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print("[+] Contract Deployed Sucessfully!")
    print("[.] Contract Address: " + str(fundme))


def main():
    deploy_fundme()
