from scripts.helpfull_scripts import get_account
from scripts.deploy import deploy_fundme
from brownie import FundMe

## fund and withdraw test is not working for some reason !! ?


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = (
        deploy_fundme()
    )  ## something is not right here , getEntraceFee is not accessible
    entrance_fee = fund_me.getEntranceFee()

    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0
