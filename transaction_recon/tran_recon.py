import pandas as pd

LEFT_COLUMN_MAPPING = {
    "id_left": "id",
    "amount_left": "amount",
    "date_left": "date",
}

RIGHT_COLUMN_MAPPING = {
    "id_right": "id",
    "amount_right": "amount",
    "date_right": "date",
}


def create_df_from_dict(data_left, data_right):
    df_left = pd.DataFrame(data_left)
    df_right = pd.DataFrame(data_right)

    df_left = df_left.rename(columns=LEFT_COLUMN_MAPPING)
    df_right = df_right.rename(columns=RIGHT_COLUMN_MAPPING)

    return df_left, df_right


def transaction_processing(source_left, source_right):
    common_transactions = pd.merge(
        source_left,
        source_right,
        left_on=list(source_left.columns),
        right_on=list(source_right.columns)
    ).reset_index(drop=True)

    left_exclusive_transactions = (
        pd.merge(
            source_left,
            source_right,
            left_on=list(source_left.columns),
            right_on=list(source_right.columns),
            how="left",
            indicator=True,
        )
        .query('_merge == "left_only"')
        .drop("_merge", axis=1)
    ).reset_index(drop=True)

    right_exclusive_transactions = (
        pd.merge(
            source_left,
            source_right,
            left_on=list(source_left.columns),
            right_on=list(source_right.columns),
            how="right",
            indicator=True,
        )
        .query('_merge == "right_only"')
        .drop("_merge", axis=1)
    ).reset_index(drop=True)

    return common_transactions, left_exclusive_transactions, right_exclusive_transactions


if __name__ == "__main__":

    input_left = {
        "id_left": [1, 2],
        "amount_left": [100, 150],
        "date_left": ["2023-01-01", "2023-01-02"],
    }

    input_right = {
        "id_right": [1, 3],
        "amount_right": [100, 200],
        "date_right": ["2023-01-01", "2023-01-03"],
    }

    source_left_df, source_right_df = create_df_from_dict(
        data_left=input_left, data_right=input_right
    )
    common_df, left_exclusive_df, right_exclusive_df = transaction_processing(
        source_left=source_left_df, source_right=source_right_df
    )

    # Print the results
    print("Common Transactions:")
    print(common_df)

    print("\nTransactions Exclusive to Left Source:")
    print(left_exclusive_df)

    print("\nTransactions Exclusive to Right Source:")
    print(right_exclusive_df)
