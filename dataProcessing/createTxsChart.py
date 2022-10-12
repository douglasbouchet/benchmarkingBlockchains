# This script is ised

import json
import matplotlib.pyplot as plt

loaded = json.load(open("inputCreateTxsChart/txs.txt"))


def addToDict(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1


def main():

    nSubmitted = 0
    nCommitted = 0

    secondToSubmittedTxs = {}
    secondToCommitedTxs = {}

    txs = loaded["Locations"][0]["Clients"][0]["Interactions"]
    # print(txs)

    for tx in txs:
        submitTime = int(tx["SubmitTime"])
        commitTime = int(tx["CommitTime"])

        if submitTime == -1:
            print("SubmtTime is -1, handle it")
            exit(1)

        nSubmitted += 1
        # add the submit time to the dict
        addToDict(secondToSubmittedTxs, submitTime)
        # same thing for commit time
        if commitTime != -1:
            addToDict(secondToCommitedTxs, commitTime)
            nCommitted += 1
        # else, the tx was not committed

        # print(submitTime, commitTime)

    # we plot the number of txs submitted/commited per second as a histogram
    # print(secondToSubmittedTxs.values())
    # print(secondToSubmittedTxs.keys())
    # print(secondToCommitedTxs.values())
    # print(secondToCommitedTxs.keys())
    plt.figure(figsize=(8, 6))
    plt.plot(
        secondToSubmittedTxs.keys(),
        secondToSubmittedTxs.values(),
        label="submited txs",
        color="y",
    )
    plt.plot(
        secondToCommitedTxs.keys(),
        secondToCommitedTxs.values(),
        label="commited txs",
        color="g",
    )
    # some tuning
    plt.xlabel("Time (s)", size=14)
    plt.ylabel("Number of transactions", size=14)
    plt.title("Plot of transactions submitted and commited")
    plt.legend(loc="upper right")
    # plt.savefig("overlapping_histograms_with_matplotlib_Python.png")

    plt.show()


if __name__ == "__main__":
    main()
