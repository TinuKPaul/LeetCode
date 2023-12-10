
def transaction_processing(source_left, source_right, mapping):
    transactions_left = {}
    transactions_right = {}

    for transaction_left in source_left:
        key = tuple(transaction_left[col] for col in mapping["left"])
        transactions_left[key] = transaction_left

    for transaction_right in source_right:
        key = tuple(transaction_right[col] for col in mapping["right"])
        transactions_right[key] = transaction_right

    common_transactions = []
    left_exclusive_transactions = []
    right_exclusive_transactions = []

    for key, transaction_left in transactions_left.items():
        if key in transactions_right:
            # Common transaction
            common_transactions.append(transaction_left)
        else:
            # Transaction exclusive to the left source
            left_exclusive_transactions.append(transaction_left)

    for key, transaction_right in transactions_right.items():
        if key not in transactions_left:
            # Transaction exclusive to the right source
            right_exclusive_transactions.append(transaction_right)

    return (
        common_transactions,
        left_exclusive_transactions,
        right_exclusive_transactions,
    )


if __name__ == "__main__":
    input_left = [
        {"id_left": 1, "amount_left": 100, "date_left": "2023-01-01"},
        {"id_left": 2, "amount_left": 150, "date_left": "2023-01-02"},
    ]

    input_right = [
        {"id_right": 1, "amount_right": 100, "date_right": "2023-01-01"},
        {"id_right": 3, "amount_right": 200, "date_right": "2023-01-03"},
    ]

    column_mapping = {
        "left": ["id_left", "amount_left", "date_left"],
        "right": ["id_right", "amount_right", "date_right"],
    }

    common_df, left_exclusive_df, right_exclusive_df = transaction_processing(
        source_left=input_left, source_right=input_right, mapping=column_mapping
    )

    print("Common Transactions:")
    print(common_df)

    print("\nTransactions Exclusive to Left Source:")
    print(left_exclusive_df)

    print("\nTransactions Exclusive to Right Source:")
    print(right_exclusive_df)
