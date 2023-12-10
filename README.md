# Transaction Recon

Time Complexity : Linear Time 

## With DataFrames
### Identifying Common Transactions (pd.merge):

The pd.merge operation has a time complexity of O(m + n), where m and n are the sizes of the two DataFrames being merged. In this case, it's O(len(source_left) + len(source_right)).

### Identifying Exclusive Transactions (pd.merge with filters):

The operations for identifying exclusive transactions involve additional pd.merge operations and filtering, but the time complexity is still O(m + n) for each of the three cases (common, left exclusive, and right exclusive).


## With Dictionaries:

### Identifying Common and Exclusive Transactions:

The subsequent loop iterates over the keys of transactions_left and transactions_right. Since dictionary lookups have an average time complexity of O(1), the overall time complexity for this part is O(n).

