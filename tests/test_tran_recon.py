import pandas as pd

from transaction_recon.tran_recon import create_df_from_dict, transaction_processing


def test_create_df_from_dict(input_dicts):
    data_left, data_right = input_dicts
    df_left, df_right = create_df_from_dict(data_left, data_right)
    assert isinstance(df_left, pd.DataFrame)
    assert isinstance(df_right, pd.DataFrame)
    assert list(df_left.columns) == ["id", "amount", "date"]
    assert list(df_right.columns) == ["id", "amount", "date"]


def test_transaction_processing(input_dfs, output_dfs):
    df_left, df_right = input_dfs
    input_common_df, input_left_exclusive_df, input_right_exclusive_df = output_dfs
    common_df, left_exclusive_df, right_exclusive_df = transaction_processing(df_left, df_right)
    assert input_common_df.equals(common_df)
    assert input_left_exclusive_df.equals(left_exclusive_df)
    assert input_right_exclusive_df.equals(right_exclusive_df)
