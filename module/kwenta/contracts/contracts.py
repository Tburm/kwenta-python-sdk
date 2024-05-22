import json
import os

# read abi files
with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/PerpsV2MarketData.json"
) as json_file:
    PerpsV2MarketData_abi = json.load(json_file)

with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/PerpsV2Market.json"
) as json_file:
    PerpsV2Market_abi = json.load(json_file)

with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/PerpsV2ExchangeRate.json"
) as json_file:
    PerpsV2ExchangeRate_abi = json.load(json_file)

with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/PerpsV2MarketSettings.json"
) as json_file:
    PerpsV2MarketSettings_abi = json.load(json_file)

with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/PerpsV2MarketState.json"
) as json_file:
    PerpsV2MarketState_abi = json.load(json_file)

with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/PerpsV2MarketViews.json"
) as json_file:
    PerpsV2MarketViews_abi = json.load(json_file)

with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/SMFactory.json"
) as json_file:
    SMFactory_abi = json.load(json_file)

with open(f"{os.path.dirname(os.path.abspath(__file__))}/json/sUSD.json") as json_file:
    sUSD_abi = json.load(json_file)

with open(
    f"{os.path.dirname(os.path.abspath(__file__))}/json/SMAccount.json"
) as json_file:
    SM_Account_abi = json.load(json_file)


# create dictionaries
addresses = {
    "sUSD": {
        10: "0x8c6f28f2f1a3c87f0f938b96d27520d9751ec8d9",
        420: "0xeBaEAAD9236615542844adC5c149F86C36aD1136",
        11155420: "0xD7D674d80e79CF3A3b67D6a510AC1B0493dF47cF",
    },
    "PerpsV2MarketData": {
        10: "0x58e6227510F83d3F45B339F2f7A05a699fDEE6D4",
        420: "0xcE2dC389fc8Be231beECED1D900881e38596d7b2",
        11155420: "0x2D19525051C491CD6F48e22a11E7e484aC172FCE",
    },
    "PerpsV2MarketSettings": {
        10: "0x649F44CAC3276557D03223Dbf6395Af65b11c11c",
        11155420: "0x34ffA8af41B1B3077e7b40cC19B6906c3125Cd0c",
    },
    "PerpsV2ExchangeRate": {
        10: "0x2C15259D4886e2C0946f9aB7a5E389c86b3c3b04",
    },
    "SMFactory": {
        10: "0x8234F990b149Ae59416dc260305E565e5DAfEb54",
        11155420: "0xF877315CfC91E69e7f4c308ec312cf91D66a095F",
    },
}

abis = {
    "sUSD": sUSD_abi,
    "PerpsV2Market": PerpsV2Market_abi,
    "PerpsV2MarketData": PerpsV2MarketData_abi,
    "PerpsV2MarketSettings": PerpsV2MarketSettings_abi,
    "PerpsV2MarketViews": PerpsV2MarketViews_abi,
    "PerpsV2MarketState": PerpsV2MarketState_abi,
    "PerpsV2ExchangeRate": PerpsV2ExchangeRate_abi,
    "SMFactory": SMFactory_abi,
    "SM_Account": SM_Account_abi,
}
