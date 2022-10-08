import json
import yaml
import pandas as pd
from ruamel.yaml import YAML
from collections import OrderedDict

workloadName = "nftix"
loaded = json.load(open('data/data_mint_20363134_22000000.json'))
startTime = loaded[0]["timeStamp"]
df = pd.DataFrame.from_records(loaded, index='id')

# substract startTime from all timestamps
df['timeStamp'] = df['timeStamp'] - startTime

# group the elements of df by timeStamp and count how many elements are in each group
df = df.groupby('timeStamp').size().reset_index(name='count')

# put each count of df inside data['workloads'][0]['client']['behavior'][0]['load'] with its timestamp
yaml = YAML()
with open('counter.yaml') as file:
    data = yaml.load(file)
    for index, row in df.iterrows():
       data['workloads'][0]['client']['behavior'][0]['load'][int(row['timeStamp'])] = int(row['count'])
       data['workloads'][0]['client']['behavior'][0]['load'][int(row['timeStamp'])+1] = 0

    with open('workload_{}.yaml'.format(workloadName), 'w') as out:
        yaml.dump(data, out)

print("Don't forget tu update the contract name and method called inside the generated workload")