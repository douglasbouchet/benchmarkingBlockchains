import json
from ruamel.yaml import YAML

# use awk '{v=$2; gsub(/[$,]/, "", v)} v+0>4000' res.yaml to obtain line with values > 4000


def main():
    # workloadPath = "pixelWarData/test.yaml"
    workloadPath = "./pixelWarData/res.yaml"
    samples = [
        [i for i in range(50000, 50300)],
        [i for i in range(203330, 203630)],
        [i for i in range(291790, 292090)],
    ]  # select here the samples you want to use
    # print(samples)
    workload = {}

    yaml = YAML()
    with open(workloadPath) as workloadFile:
        data = yaml.load(workloadFile)
        # txs = data["workloads"][0]["client"]["behavior"][0]["load"]
        # print(data)
        txs = data[2]["txs"]
        nElem = 0
        for sample in samples:
            for i in sample:
                if i in txs:
                    workload[nElem] = txs[i]
                    # print(txs[i])
                else:
                    workload[nElem] = 0
                nElem += 1

    # print(workload)

    with open("concatenated.yaml", "w") as outYaml:
        yaml.dump(workload, outYaml)


if __name__ == "__main__":
    main()
