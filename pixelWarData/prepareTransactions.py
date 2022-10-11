# we count the number of transactions happening each second and write this number in a yaml file which represent
# the transactions per second we will used to benchMark the blockchains

# For the arguments, I simplified them as one unique for each transactions happening at the same second.
# possible to make one for each txs but longer...

# format
#
# txs:
#   0:140
#   1:78
#   2:45...
#
# arguments: (second, x, y, color)
#
#   0,687,1843,#94B3FF
#   1,240,1052,#6A5CFF
#   2,602,1488,#94B3FF

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
    # csv_values = []
    translated_csv_values = {}

    with open("function-arguments.csv", "w") as csv_file:
        # we iterate over each of the 78 csv files:
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

                    if currentSecond not in translated_csv_values:
                        # we also record which pixels where being placed by the user
                        splitted = line.split(",")
                        color = splitted[-3]
                        coordinates = splitted[-2:]
                        x = coordinates[0].replace('"', "")
                        y = coordinates[1].replace('"', "").replace("\n", "")
                        # print(int(x), int(y))
                        # write x,y and color into a csv file
                        # csv_values.append(
                        #    str(currentSecond) + "," + x + "," + y + "," + color
                        # )
                        translated_csv_values[currentSecond] = x + "," + y + "," + color

    # print(secondToTxs)

    # we scale the keys by the first second (this we start at 0)
    start_second = min(secondToTxs.keys())
    final_dict = {}
    final_values = {}

    for key in secondToTxs.keys():
        final_dict[key - start_second] = secondToTxs[key]

with open("arguments.csv", "w") as csv_file:
    for key in translated_csv_values.keys():
        # final_values[key - start_second] = translated_csv_values[key]
        csv_file.write(
            str(key - start_second) + "," + translated_csv_values[key] + "\n"
        )

    # now we can write the yaml file
    dict_file = [
        {"id": "PixelWar"},
        {"contract": "pixelWar:setPixel"},
        {"txs": final_dict},
    ]

    with open(r"res.yaml", "w") as file:
        documents = yaml.dump(dict_file, file)
