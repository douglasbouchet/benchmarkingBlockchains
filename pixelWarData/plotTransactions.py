import matplotlib.pyplot as plt
import yaml
from yaml.loader import SafeLoader

if __name__ == "__main__":

    # Open the file and load the file
    with open('res.yaml') as f:
        data = yaml.load(f, Loader=SafeLoader)

        print("data loaded")
        transactions = data[2]['txs']

        txs_time = []
        txs_nb = []

        for i, elem in enumerate(transactions):
            if(i % 1000 == 0):
                print(i)
            txs_time.append(elem)
            txs_nb.append(transactions[elem])
            #print(elem, transactions[elem])

        plt.plot(txs_time, txs_nb)
        plt.savefig("transactions.png")
        # plt.show()


# 210478: 1220
