# Downloading the data

data can be found from this page ["https://www.reddit.com/r/place/comments/txvk2d/rplace_datasets_april_fools_2022/"]

## Benchmarking:

We will select 3 phases of the pixel war:
- One with a quite low number of transactions (around 500 per seconds). From 50000 to 50300 seconds.
- One with a higher number of transactions (spike ~ 5000 per seconds). From 203330 to 203630 seconds.
- One with the highest number of transactions (spike ~ 8000 per seconds). From 291790 to 292090 seconds.

We then concatenate these phases and run them on the quorum blockchain.

We obtained the following results:
