import requests
import json
import time

username = "DougyDoug"
apiKey = "9KFNTEZ9Y7K38AXTDC6JBEH5MCMU8DKQR5"
#smartContractAddress = "0x08c2af3f01a36ad9f274cce77f6f77cf9aa1dfc9"
# smartContractAddress = "0xbce1b23c7544422f1e2208d29a6a3aa9fabab250" # mint: TicketProvider
# smartContractAddress = "0x63a54ecee15ea9dca53b32a2c25df33120edf099" # mint: Guts
# smartContractAddress = "0x55a4e122cf740b7cf8991262d4231ffb6951dc76" # mint: Relic Ticket
# smartContractAddress = "0x498801c981985016bd5a62facf0b41df1913fdbe" # mint: NeonOx
# smartContractAddress = "0x53e91328b5774485a8c033daf0ef5952a7588a58" # mint ?

providerToSmartContractAddress = {'TicketProvider': "0xbce1b23c7544422f1e2208d29a6a3aa9fabab250",
                                  'Guts': "0x63a54ecee15ea9dca53b32a2c25df33120edf099",
                                  'Relic Ticket': "0x55a4e122cf740b7cf8991262d4231ffb6951dc76",
                                  'NeonOx': "0x498801c981985016bd5a62facf0b41df1913fdbe"}


def getTxs(fromBlock, untilBlock, smartContractAddress, username, apiKey):
    url = "https://api.polygonscan.com/api?module=logs&action=getLogs&fromBlock={}&toBlock={}&address={}&apikey={}".format(
        fromBlock, untilBlock, smartContractAddress, apiKey)
    r = requests.get(url, auth=(username, apiKey))
    return r.json()


def processJson(_json, counter):
    """ Process the json response from the API
    Keep only the timeStamp and add an Id to each transaction.
    Here each transaction represent a call to the smart contract used to sell the NFTix tickets.

    Args:
        json (json): json response from the API
    """
    data = []
    for i, tx in enumerate(_json["result"]):
        data.append(
            json.dumps({"id": counter, "timeStamp": int(tx["timeStamp"], base=16), "blockNumber": int(tx["blockNumber"], base=16)}))
        counter += 1

    return data


def fetchAllData():
    # startBlock = 20363134  # before this block, the smart contract was not deployed
    # startBlock = 33763134  # before this block, the smart contract was not deployed for mint
    #endBlock = 24263134
    startBlock = 33898424  # ~ actual
    endBlock = 33909989  # ~ actual
    #blockCheckPerQuery = 2000
    blockCheckPerQuery = 10000
    totalData = []
    counter = 0  # Usefull to assign on id to each transaction
    for key in providerToSmartContractAddress:
        c = 0
        for i in range(startBlock, endBlock, blockCheckPerQuery):
            print("Fetching data from block {} to {}".format(
                i, i + blockCheckPerQuery))
            res = getTxs(i, i + blockCheckPerQuery,
                         providerToSmartContractAddress[key], username, apiKey)
            data = processJson(res, counter)
            totalData.extend(data)
            counter += len(data)
            c += len(data)
            print("The number of transactions for {} is: {}".format(key, len(data)))

        print("The total number of transactions for {} is: {}".format(key, c))

    print("The total number of transactions is: {}".format(len(totalData)))
    with open('data_mint_{}_{}.json'.format(startBlock, endBlock), 'w') as out:
        json.dump(totalData, out, indent=6)


fetchAllData()
