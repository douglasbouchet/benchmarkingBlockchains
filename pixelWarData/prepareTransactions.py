# we count the number of transactions happening each second and write this number in a yaml file which represent
# the transactions per second we will used to benchMark the blockchains

# TODO not sure of the expected form of the yaml file, see with Gauthier

# format
#
# txs:
#   0:140
#   1:78
#   2:45...

import yaml
from datetime import datetime


def computeSeconds(year, month, day, hour, minute, second):
    # print(year, month, day, hour, minute, second)
    return int(datetime(year, month, day, hour, minute, second).timestamp())


def addSecondToDict(d, second):
    if second in d:
        d[second] += 1
    else:
        d[second] = 1


if __name__ == "__main__":

    secondToTxs = {}

    with open("function-arguments.csv", "w") as csv_file:
        # we iterate over each of the 78 csv files:
        # for fileId in range(0, 79):
        # for fileId in range(1, 79):
        for fileId in range(1, 2):
            print("fileId: ", fileId)
            filename = "data/" + str(fileId) + ".csv"
            with open(filename, "r") as f:
                f.readline()  # skip the headers
                for line in f:
                    # we get the time of the transaction
                    splitted = line.split(" ")
                    day_data = splitted[0].split("-")
                    year = int(day_data[0])
                    month = int(day_data[1])
                    day = int(day_data[2])
                    hour_data = splitted[1].split(":")
                    hour = int(hour_data[0])
                    minute = int(hour_data[1])
                    second = int(hour_data[2].split(".")[0])
                    # we compute how much second does that represent
                    currentSecond = computeSeconds(
                        year, month, day, hour, minute, second
                    )
                    # print("second: ", computeSeconds(
                    #    year, month, day, hour, minute, second))
                    addSecondToDict(secondToTxs, currentSecond)

                    # we also record which pixels where being placed by the user
                    splitted = line.split(",")
                    color = splitted[-3]
                    coordinates = splitted[-2:]
                    x = coordinates[0].replace('"', "")
                    y = coordinates[1].replace('"', "").replace("\n", "")
                    # print(int(x), int(y))
                    # write x,y and color into a csv file
                    csv_file.write(x + "," + y + "," + color + "\n")

    # print(secondToTxs)

    # we scala the keys by the first second (this we start at 0)
    start_second = min(secondToTxs.keys())
    final_dict = {}

    for key in secondToTxs.keys():
        final_dict[key - start_second] = secondToTxs[key]

    # print(final_dict)
    # now we can write the yaml file

    dict_file = [
        {"id": "PixelWar"},
        {"contract": "pixelWar:setPixel"},
        {"txs": final_dict},
    ]

    with open(r"res.yaml", "w") as file:
        documents = yaml.dump(dict_file, file)
