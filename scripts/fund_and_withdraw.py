from msilib.schema import Error
from black import err
from brownie import FundMe
from scripts.helpfull_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    print(f"[+] Accessing the Deployed Contract: {str(fund_me)}")
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(f"[.] The Current entry fee is {entrance_fee}")
    try:
        print("[+] Funding ...")
        fund_me.fund({"from": account, "value": entrance_fee})
        print(f"[+] {entrance_fee} Value Funded !! ")
    except Exception as ex:
        print(f"Error: {ex}")
        exit(1)


def withdraw():
    print("\n[+] Withdrawing ..!")
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("[+] Value Withdrawed")


def main():
    fund()
    withdraw()
